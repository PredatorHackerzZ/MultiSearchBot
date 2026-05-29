# (c) MrAbhi2k3 and PredatorHackerzz
# https://github.com/PredatorHackerzZ/MultiSearchBot

import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SESSION_NAME = os.environ.get("SESSION_NAME", "MultiSearchBot")
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1287407305))
    FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "-1001299900751")
    SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "-1001429962431")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001299900751")
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb://localhost:27017")
    DB_NAME = os.environ.get("DB_NAME", "multisearch_bot")
    
    TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "77")
    
    TORRENT_APIS = {
        "piratebay": "https://magnetz.eu/api/magnets/search?query=",
        "1337x": "https://torrents-api.xyz/torrents?query=",
        "yts": "https://yts.mx/api/v2/list_movies.json?query=",
        "nyaa": "https://nyaa.si/api/v1/search?q="
    }
    
    MUSIC_APIS = {
        "jiosaavn": "https://jiosaavn-apix.arcadopredator.workers.dev",
        "ytdl": "https://base-api-three-alpha.vercel.app/api/download/ytdl?url="
    }
    
    MOVIE_APIS = {
        "jikan": "https://api.jikan.moe/v4",
        "tmdb": "https://api.themoviedb.org/3",
        "vidfast": "https://vidfast.pro",
        "vidlink": "https://vidlink.pro"
    }
    
    STREAMING_EMBEDS = {
        "vidfast": "https://vidfast.pro/movie/{id}?autoPlay=true&title=true&poster=true",
        "vidlink": "https://vidlink.pro/movie?tmdb={id}"
    }
    
    TIKTOK_API = "https://www.tikwm.com/api/"
