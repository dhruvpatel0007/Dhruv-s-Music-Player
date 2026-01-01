# Python Music Player - Setup Guide by Dhruv

## Prerequisites

### 1. Install Python
- Download from [python.org](https://www.python.org/downloads/)
- ✅ **IMPORTANT**: Check "Add Python to PATH" during installation

### 2. Install VLC Media Player
- Download from [videolan.org](https://www.videolan.org/)
- ✅ **IMPORTANT**: Match architecture (64-bit Python = 64-bit VLC)

---

## Installation Commands

### Essential Libraries
Open Command Prompt or VS Code Terminal and run:

```bash
# Update pip
python -m pip install --upgrade pip

# Install required libraries
pip install yt-dlp
pip install python-vlc
pip install requests
pip install Pillow

# For GUI (if needed)
pip install customtkinter
```

### Update Existing Libraries
```bash
pip install --upgrade yt-dlp
pip install --upgrade python-vlc
```

---

## Fix HTTP 403 Error

### Updated Code Template

```python
import yt_dlp
import vlc

# Configuration for Edge browser
ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'cookiesfrombrowser': ('edge',),  # Use Edge cookies
    'extractor_args': {'youtube': {'player_client': ['android']}},
}

def play_youtube_audio(youtube_url):
    try:
        # Extract audio URL
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            audio_url = info['url']
        
        # Play audio
        player = vlc.MediaPlayer(audio_url)
        player.play()
        return player
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
player = play_youtube_audio("YOUR_YOUTUBE_URL_HERE")
```

---

## Common Import Statements

```python
import yt_dlp
import vlc
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests
from PIL import Image, ImageTk
```

---

## Verification Test

```python
# Run this to verify installation
try:
    import yt_dlp
    import vlc
    import tkinter
    print("✅ All libraries installed successfully!")
except ImportError as e:
    print(f"❌ Missing library: {e}")
```

---

## Quick Troubleshooting

| Error | Solution |
|-------|----------|
| HTTP 403 | Update yt-dlp: `pip install --upgrade yt-dlp` |
| VLC not found | Install VLC Media Player (match Python architecture) |
| Import Error | Run: `pip install <missing-library>` |
| Cookies issue | Add `'cookiesfrombrowser': ('edge',)` to options |

---

## Complete Setup Checklist

- [ ] Python installed (with PATH)
- [ ] VLC Media Player installed (matching architecture)
- [ ] Run: `pip install yt-dlp python-vlc`
- [ ] Run: `pip install --upgrade yt-dlp`
- [ ] Added Edge cookies to code
- [ ] Tested with verification script

---

**Note**: YouTube frequently updates their API. Always keep `yt-dlp` updated using:
```bash
pip install --upgrade yt-dlp
```

---

*For additional help, visit: [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp)*