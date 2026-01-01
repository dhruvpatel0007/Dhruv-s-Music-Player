# 🎵 Dhruv Music Player

A modern, lightweight desktop application that brings YouTube's vast music library directly to your fingertips. Built with Python, featuring an elegant GUI interface powered by Tkinter and VLC media player for seamless audio streaming.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📖 About The Project

Dhruv Music Player eliminates the need for downloading songs or switching between browser tabs. Simply search, click, and enjoy your favorite music instantly. The application combines the convenience of a dedicated music player with the endless variety of YouTube, all wrapped in an elegant and user-friendly interface.

### ✨ Key Features

- 🔍 **Instant Search** - Search any song directly from YouTube with lightning-fast results
- 🎨 **Dynamic Cover Art** - Automatically fetches and displays song thumbnails
- ⏯️ **Complete Playback Control** - Play, pause, and stop with intuitive buttons
- 🎧 **High-Quality Audio** - Streams the best available audio quality
- 💻 **Clean Modern Interface** - Minimalist design focused on your music
- ⚡ **Lightweight & Fast** - Uses minimal system resources
- 🆓 **Completely Free** - No subscriptions, no ads, unlimited streaming

## 🖼️ Screenshots

```
┌──────────────────────────────────────────┐
│      Dhruv Patel Music Player            │
├──────────────────────────────────────────┤
│                                          │
│  Search YouTube Song:                    │
│  [Enter song name here...    ] 🔍 Search │
│                                          │
│  ┌────────────────────────────────┐     │
│  │                                │     │
│  │        Album Cover Art         │     │
│  │         320 x 180              │     │
│  │                                │     │
│  └────────────────────────────────┘     │
│                                          │
│         Now Playing: Song Title          │
│                                          │
│         ▶️        ⏸️        ⏹️            │
│        Play      Pause      Stop         │
│                                          │
└──────────────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

Before running this application, ensure you have the following installed:

1. **Python 3.8 or higher**
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ **IMPORTANT**: Check "Add Python to PATH" during installation

2. **VLC Media Player**
   - Download from [videolan.org](https://www.videolan.org/)
   - ⚠️ **CRITICAL**: Install the same architecture as your Python (64-bit Python = 64-bit VLC)

### Installation

Follow these steps to get Dhruv Music Player running on your system:

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/dhruv-music-player.git
   cd dhruv-music-player
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update yt-dlp (Important for YouTube compatibility)**
   ```bash
   pip install --upgrade yt-dlp
   ```

4. **Run the application**
   ```bash
   python music_player.py
   ```

### Quick Install (One Command)

```bash
pip install yt-dlp python-vlc Pillow requests && pip install --upgrade yt-dlp
```

## 📦 Dependencies

This project uses the following Python libraries:

| Library | Version | Purpose |
|---------|---------|---------|
| yt-dlp | >=2023.12.30 | YouTube video/audio extraction |
| python-vlc | >=3.0.18121 | VLC media player bindings |
| Pillow | >=10.0.0 | Image processing for cover art |
| requests | >=2.31.0 | HTTP requests for thumbnails |
| tkinter | Built-in | GUI framework |

## 🎮 How to Use

### Step 1: Launch the Application
```bash
python music_player.py
```

### Step 2: Search for Music
- Enter song name, artist, or keywords in the search bar
- Examples:
  - "Bohemian Rhapsody"
  - "Ed Sheeran Shape of You"
  - "Bollywood romantic songs"

### Step 3: Enjoy!
- Click **🔍 Search & Play** button
- The player will automatically find and play the top result
- Cover art and song title will display automatically

### Playback Controls
- **▶️ Play**: Start or resume playback
- **⏸️ Pause**: Pause the current song
- **⏹️ Stop**: Stop playback completely

## 🛠️ Troubleshooting

### Problem: HTTP 403 Error

**Solution**: Update your code with browser cookies

```python
# In music_player.py, modify ydl_opts to include:
ydl_opts = {
    'default_search': 'ytsearch',
    'format': 'bestaudio',
    'quiet': True,
    'noplaylist': True,
    'cookiesfrombrowser': ('edge',),  # or 'chrome', 'firefox'
    'extractor_args': {'youtube': {'player_client': ['android']}},
}
```

### Problem: VLC Media Player Not Found

**Solutions**:
- Verify VLC is installed: Check `C:\Program Files\VideoLAN\VLC\` (Windows)
- Ensure architecture matches (64-bit Python needs 64-bit VLC)
- Reinstall VLC with default settings

### Problem: Module Not Found Errors

```bash
# Reinstall all dependencies
pip install --upgrade yt-dlp python-vlc Pillow requests
```

### Problem: Search Takes Too Long

**Solutions**:
- Check your internet connection
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Try searching with more specific keywords

## 🔧 Configuration

### Custom Window Size
Edit in `music_player.py`:
```python
self.root.geometry("460x550")  # Change width x height
```

### Change Theme Colors
Modify button colors:
```python
bg="#1db954"  # Background color (Spotify Green)
fg="white"    # Text color
```

## 💡 Future Enhancements

Planned features for upcoming versions:

- [ ] Volume control slider
- [ ] Progress bar with seek functionality
- [ ] Playlist creation and management
- [ ] Download songs for offline listening
- [ ] Search history and favorites
- [ ] Lyrics display integration
- [ ] Dark/Light theme toggle
- [ ] Mini player mode
- [ ] Keyboard shortcuts
- [ ] Equalizer settings

## 🤝 Contributing

Contributions make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your Changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the Branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

## 👨‍💻 Author

**Dhruv Patel**

- GitHub: [@YOUR_GITHUB_USERNAME](https://github.com/YOUR_USERNAME)
- Project Link: [https://github.com/YOUR_USERNAME/dhruv-music-player](https://github.com/YOUR_USERNAME/dhruv-music-player)

## 🙏 Acknowledgments

Special thanks to these amazing projects:

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Powerful YouTube extraction tool
- [VLC Media Player](https://www.videolan.org/) - Robust media playback engine
- [Python](https://www.python.org/) - The language that powers it all
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI library

## ⚠️ Disclaimer

This application is intended for **educational purposes only**. Please respect:
- YouTube's Terms of Service
- Copyright laws and intellectual property rights
- Content creators' rights

Only stream content that you have the legal right to access.

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](https://github.com/YOUR_USERNAME/dhruv-music-player/issues)
3. Create a new issue with detailed information

## ⭐ Show Your Support

If you found this project helpful or interesting:
- Give it a ⭐ on GitHub
- Share it with friends
- Fork it and build something cool!

---

<div align="center">

**Made with ❤️ by Dhruv Patel**

[Report Bug](https://github.com/YOUR_USERNAME/dhruv-music-player/issues) · [Request Feature](https://github.com/YOUR_USERNAME/dhruv-music-player/issues)

</div>
