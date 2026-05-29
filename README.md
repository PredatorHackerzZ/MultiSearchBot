# 🤖 MultiSearch Bot - Telegram Search Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Framework](https://img.shields.io/badge/Framework-Pyrogram-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

A **lightweight, high-performance** Telegram bot for searching torrents, movies, music, anime, and more with beautiful UI/UX!

**Developers:** [@MrAbhi2k3](https://github.com/MrAbhi2k3), [@PredatorHackerzz](https://github.com/PredatorHackerzZ)

---

## ✨ What Can It Do?

- 🔥 **Multi-Source Torrent Search** - PirateBay, 1337x, YTS, Nyaa.si with magnet links
- 🎬 **Movie & TV Search** - TMDB integration with online streaming embeds
- 🎵 **Music Search** - JioSaavn integration, songs, artists, albums
- 🎌 **Anime Database** - Jikan API with complete series information
- 📱 **TikTok & YouTube** - Video search and downloads
- 📊 **User Tracking** - Search history, statistics, activity logging
- 🏷️ **Advanced Filtering** - Quality (1080p, 720p), language, genre filters
- ⚡ **Lightning Fast** - Async API calls, global configuration, optimized responses
- 🎨 **Beautiful UI** - Inline buttons with professional design

---

## 🚀 Quick Start (30 seconds)

### Step 1: Get Credentials
1. Get Telegram API: https://my.telegram.org/
2. Create bot with @BotFather: Get BOT_TOKEN
3. (Optional) Get TMDB API: https://www.themoviedb.org/settings/api

### Step 2: Install & Run
```bash
# Clone
git clone https://github.com/PredatorHackerzZ/MultiSearchBot.git
cd MultiSearchBot

# Install (Windows: use install.bat)
bash install.sh

# Configure
nano .env

# Run
python main.py
```

---

## 📚 Complete Documentation

| Document | Purpose |
|----------|---------|
| **[USER_MANUAL.md](USER_MANUAL.md)** | Complete guide with 300+ lines - All commands, filters, features |
| **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** | Cheat sheet - Common commands & examples |
| **[README_SETUP.md](README_SETUP.md)** | Installation & features overview |
| **[DEPLOYMENT.md](DEPLOYMENT.md)** | Deploy to Heroku, Docker, VPS, Railway, Replit |

---

## 💡 Usage Examples

### Inline Search (Recommended)
Type in any Telegram chat:

```
@MultiSearchXBot !movie avengers 1080p
@MultiSearchXBot !pb ubuntu iso
@MultiSearchXBot !music imagine dragons
@MultiSearchXBot !anime naruto english
```

### Direct Commands
In bot private chat:

```
/start         - Start bot
/help          - Full help
/stats         - Bot statistics
/my_searches   - Your history
```

---

## 🔍 Search Commands

### 🎬 Movies & Shows
```
!movie [name]              Search movies + streaming links
!anime [name]              Anime series info
!tmdb [name]               Detailed movie info
```

### 🔥 Torrents
```
!pb [name]                 PirateBay torrents
!1337x [name]              1337x torrents
!yts [name]                YTS movie torrents
!nyaa [name]               Nyaa anime torrents
```

### 🎵 Music
```
!music [song]              Search songs
!artist [name]             Find artists
!album [name]              Album tracks
```

### 📱 Videos
```
!tiktok [query]            TikTok videos
!youtube [query]           YouTube videos
```

---

## 🏷️ Filters & Tags

### Quality
```
1080p, 720p, 480p, 4K, HD
```

### Language
```
ENGLISH, HINDI, TAMIL, DUBBED, SUBTITLED
```

### Genre
```
ACTION, COMEDY, THRILLER, HORROR, ROMANCE, DRAMA
```

### Release
```
LATEST, POPULAR, NEW, CLASSIC
```

### Examples
```
@bot !movie avengers 1080p english latest
@bot !pb ubuntu 1080p popular
@bot !music hindi songs new
```

---

## 📡 API Integrations

| Feature | API | Status |
|---------|-----|--------|
| Torrents | Magnetz (PirateBay) | ✅ Working |
| Torrents | 1337x | ✅ Working |
| Movies | YTS | ✅ Working |
| Anime | Nyaa.si | ✅ Working |
| Anime | Jikan | ✅ Working |
| Movies | TMDB | ✅ Configured |
| Music | JioSaavn | ✅ Working |
| Streaming | VidFast | ✅ Embeds |
| Streaming | VidLink | ✅ Embeds |
| Video | TikTok | ✅ Working |

---

## ⚙️ Configuration

All APIs and settings use **global variables** in `configs.py`. Set via `.env` file:

```env
API_ID=123456789
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
TMDB_API_KEY=your_tmdb_key
OWNER_ID=0
FORCE_SUB_CHANNEL=
SUPPORT_GROUP=
UPDATE_CHANNEL=
```

---

## 🚀 Deployment Options

### 1. Local (Development)
```bash
python3 main.py
```

### 2. Docker
```bash
docker build -t multisearch-bot .
docker run -e BOT_TOKEN=xxx -e API_ID=xxx multisearch-bot
```

### 3. Heroku / Railway / Replit / VPS

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed guides

---

## 🧪 Testing APIs

```bash
python3 test_apis.py
```

---

## 📊 Commands Summary

| Category | Commands |
|----------|----------|
| **Direct** | /start, /help, /about, /stats, /start_track |
| **Torrents** | !pb, !1337x, !yts, !nyaa |
| **Movies** | !movie, !anime, !tmdb |
| **Music** | !music, !artist, !album |
| **Video** | !tiktok, !youtube |

---

## 📞 Support & Community

| Platform | Link |
|----------|------|
| **GitHub** | https://github.com/PredatorHackerzZ/MultiSearchBot |
| **Telegram Bot** | @MultiSearchXBot |
| **Support Group** | @TeleRoid14 |
| **Updates Channel** | @TeleRoidGroup |

---

## 🤝 Credits

**Developers:**
- [@MrAbhi2k3](https://github.com/MrAbhi2k3)
- [@PredatorHackerzz](https://github.com/PredatorHackerzZ)

---

<div align="center">

### 🚀 Ready to Use?

**[📚 Read USER_MANUAL.md](USER_MANUAL.md)** → **[⚡ QUICK_REFERENCE.md](QUICK_REFERENCE.md)** → **[🚢 DEPLOYMENT.md](DEPLOYMENT.md)**

Made with ❤️ for the Telegram community

</div>
