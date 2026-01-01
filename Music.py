import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import yt_dlp
import vlc
import threading
import io

class SimpleYTPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title(" Dhruv Patel Music PLayer")
        self.root.geometry("460x550")
        self.player = None
        self.audio_url = None

        # Search Bar
        tk.Label(root, text="Search YouTube Song:", font=("Montserrat", 14)).pack(pady=8)
        self.search_entry = tk.Entry(root, font=("Montserrat", 13), width=28)
        self.search_entry.pack()
        self.search_btn = tk.Button(root, text="🔍 Search & Play", font=("Montserrat", 12, "bold"),
                                    bg="#1db954", fg="white", command=self.search_and_play)
        self.search_btn.pack(pady=10)

        # Cover Art
        self.cover_panel = tk.Label(root, text="No Cover", font=("Montserrat", 12), bg="#181818", fg="#fff")
        self.cover_panel.pack(fill='both', expand=False, padx=30, pady=20, ipady=5)
        
        # Song Title
        self.song_title_lbl = tk.Label(root, text="", font=("Montserrat", 12, "bold"), wraplength=400)
        self.song_title_lbl.pack()

        # Control Buttons
        bar = tk.Frame(root)
        bar.pack(pady=16)
        self.play_btn = tk.Button(bar, text="▶", font=("Arial", 20), width=5, command=self.play_audio)
        self.play_btn.grid(row=0, column=0, padx=8)
        self.pause_btn = tk.Button(bar, text="⏸", font=("Arial", 20), width=5, command=self.pause_audio)
        self.pause_btn.grid(row=0, column=1, padx=8)
        self.stop_btn = tk.Button(bar, text="⏹", font=("Arial", 20), width=5, command=self.stop_audio)
        self.stop_btn.grid(row=0, column=2, padx=8)

        # Cache state
        self.stream_url = None
        self.thumb_url = None

    def search_and_play(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showerror("Error", "Please enter a search term.")
            return
        self.song_title_lbl.config(text="Searching...")
        threading.Thread(target=self._search_worker, args=(query,), daemon=True).start()

    def _search_worker(self, query):
        try:
            # Search YouTube using yt-dlp
            ydl_opts = {
                'default_search': 'ytsearch',
                'format': 'bestaudio',
                'quiet': True,
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                if 'entries' in info:
                    entry = info['entries'][0]
                else:
                    entry = info
                self.stream_url = entry['url']
                self.thumb_url = entry.get('thumbnail', None)
                title = entry.get('title', 'Unknown Title')
        except Exception as e:
            self.song_title_lbl.config(text="Error finding song.")
            messagebox.showerror("Search Error", f"Could not search: {e}")
            return
        self.song_title_lbl.config(text=title)
        self.show_cover(self.thumb_url)
        self.play_audio()

    def show_cover(self, url):
        if not url:
            self.cover_panel.config(image='', text='No Cover')
            return
        try:
            img_bytes = requests.get(url).content
            img = Image.open(io.BytesIO(img_bytes)).resize((320, 180))
            imgTk = ImageTk.PhotoImage(img)
            self.cover_panel.config(image=imgTk, text='')
            self.cover_panel.image = imgTk
        except Exception:
            self.cover_panel.config(image='', text='No Cover')

    def play_audio(self):
        if self.stream_url:
            try:
                if self.player:
                    self.player.stop()
                self.player = vlc.MediaPlayer(self.stream_url)
                self.player.play()
            except Exception:
                messagebox.showerror("Playback Error", "Could not start playback.")

    def pause_audio(self):
        if self.player:
            self.player.pause()

    def stop_audio(self):
        if self.player:
            self.player.stop()

# Start GUI
root = tk.Tk()
app = SimpleYTPlayer(root)
root.mainloop()
