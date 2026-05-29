# (c) MrAbhi2k3 and PredatorHackerzz
# https://github.com/PredatorHackerzZ/MultiSearchBot

import aiohttp
import asyncio
from configs import Config
from requests.utils import requote_uri

async def search_torrents_magnetz(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.TORRENT_APIS['piratebay']}{query}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("magnets", [])[:Config.MAX_INLINE_RESULTS]
    except:
        pass
    return []

async def search_torrents_1337x(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.TORRENT_APIS['1337x']}{query}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("torrents", [])[:Config.MAX_INLINE_RESULTS]
    except:
        pass
    return []

async def search_torrents_yts(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.TORRENT_APIS['yts']}{query}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    movies = data.get("data", {}).get("movies", [])
                    return movies[:Config.MAX_INLINE_RESULTS]
    except:
        pass
    return []

async def search_anime_nyaa(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.TORRENT_APIS['nyaa']}{query}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("data", [])[:Config.MAX_INLINE_RESULTS]
    except:
        pass
    return []

async def search_anime_jikan(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.MOVIE_APIS['jikan']}/anime?query={query}&limit={Config.MAX_INLINE_RESULTS}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("data", [])
    except:
        pass
    return []

async def search_movies_tmdb(query: str):
    if not Config.TMDB_API_KEY:
        return []
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.MOVIE_APIS['tmdb']}/search/movie?api_key={Config.TMDB_API_KEY}&query={query}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("results", [])[:Config.MAX_INLINE_RESULTS]
    except:
        pass
    return []

async def search_music_jiosaavn(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.MUSIC_APIS['jiosaavn']}/api/search/songs?query={query}&limit={Config.MAX_INLINE_RESULTS}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("data", {}).get("results", [])
    except:
        pass
    return []

async def download_youtube_music(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            api_url = f"{Config.MUSIC_APIS['ytdl']}{url}"
            async with session.get(api_url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    return await res.json()
    except:
        pass
    return {}

async def search_tiktok(query: str):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"{Config.TIKTOK_API}search/general?keywords={query}&count={Config.MAX_INLINE_RESULTS}"
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as res:
                if res.status == 200:
                    data = await res.json()
                    return data.get("data", {}).get("videos", [])
    except:
        pass
    return []

async def get_streaming_embed(tmdb_id: str, is_tv: bool = False, season: int = 1, episode: int = 1):
    if is_tv:
        return f"{Config.STREAMING_EMBEDS['vidfast'].replace('{id}', tmdb_id)}&season={season}&episode={episode}"
    return Config.STREAMING_EMBEDS['vidfast'].replace('{id}', tmdb_id)

async def Search1337x(query: str):
    return await search_torrents_1337x(query)

async def SearchYTS(query: str):
    return await search_torrents_yts(query)

async def SearchPirateBay(query: str):
    return await search_torrents_magnetz(query)

async def SearchAnime(query: str):
    return await search_anime_jikan(query)

async def SearchPyPi(query: str):
    return []
