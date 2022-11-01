import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16201655"))
API_HASH = getenv("API_HASH", "440ba807d2cdf696ca498d441e2a6b29")
BOT_TOKEN = getenv("BOT_TOKEN", "2121214342:AAHzQBOLsqAlENXdfOYjNUJZ4ti54LUvuco")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hnyx:hny@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001853541618"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ғᴀʟʟᴇɴ ダ ᴍᴜ𝕤ɪᴄ ダ 𝕃𝕖𝕘𝕖𝕟𝕕​")
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5037053047").split())
)
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/FallenXBots")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/Y_RUS_SUPPORT")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "5900")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/SPARTENX-OP/VirusMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/ll_ll_LegendHacker_IN_ll_ll")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "7")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2073741824")
)


STRING1 = getenv("STRING_SESSION", "BQCZUZb0sVBzruHag5aJhUG87JOsSKKC-yU4jSRvoAB-sQfMBzrmaIz98lXGwP2-yQSadazaJncjsQlfCOZozKHP8qFuKF3Mcj2_3ow0b1lXCWvj1snouU187Ym2p2HYsuTRnJYklOPK4PrMdXVbqFSHwJv6Bky6ZiDHWRyupkAuU_jpdhG2xXwy_X7FLSvKk9zPftU5B_BgurZ6GhXlzSq7xYqkJEFQAwLujsm8MY8O4kKPk3A2nn1JpQApNGHUQJ5ohEjO9D1QKKQkTMTw8NkfTVV2oCSM3J2FvQQwv5nIQ7wbJC7tqkGrGkUKGAICclzEsb_iUlM_kFMqcHk_K4ezAAAAASw7VHcA")
STRING2 = getenv("STRING_SESSION2", "AQBq_3yhyNvPInV81stSwsiGriPEJbbaEW0iXcZXHKxIRFumuAl2eNqdwZpMUAFcJ5LSw4mbSKAS19-kp6mB0nZecyv9sUnHBMWgpektK7tjcIzo1YwPHYcfVrm49NQgpuRGSwR_cIt5CAweM3tIzNqFK2GsTqMIf-rOAfdido2UWgUdG25AF3IuSrORT0O3z0P6xiy7J-LE2VrQn3TaEYFVgM7hbhqE0cvKrpJUnhIvkQj-7IZ6urroIoYRlPjVaDnKw1jb984bLxARCkJz1Su8_nfx0XWBhmb3pUl6fGOE0EqNsMJzfVJBFSDJtAUlMtdQ0ZQvYzDBvV6pqnBbabH6AAAAAVIu2WgA")
STRING3 = getenv("STRING_SESSION3", "AQA7xY5Pzq3YbwX02Nu0EO7QtwoLQeRiwn0cS4tB87DIz_D7DkT6s4pNJH-jn7JJbybNJS5nIpyQXwFF0C0zr_suKC3mp3j4VzKyfBglZcrWjql-tNuB4bSGMogSCSwHLsalxrRZonHYjTHmv6b4etJkwq3fMxqIb53yDsmH01XFMW7LmpMGixXbcHGA7SyYutytm97Iqs8eNd8I92_d3aUWzsx-Eu--Uigub_jSkW8qsKoj8ABRV6T2QsOv8kg9SFHpppuQDlFg_f2mVvneE01Ksd5dHyBmYoezrPnE00GwFVuTZrbPhLvLAZNl50W89nMFrcto-8_RbtPrEGSIzO3CAAAAAVUGtKUA")
STRING4 = getenv("STRING_SESSION4", "AQBBwFjILVNwLokyBOurrbQYIi_ToC9CcuW0EI83TD0tAkCrgsV3xlE48lQRlmr9mJ8ZL8nvyT2gaAA0Yl3UwdEsmbRzkOSWtnwQuWPLIsk_PyCoOnPRLwB6jx_CP9sHX4lniBXCEXpU17ulv5TM7fFYKkeBNLNUqSkCj2GBuEZZVNS19WMHqydCUWCt8wKFa-1nM5h6sRjrCZakNHlc7yePkmJoJwAniCwjLCwWDPqaLvUHdiV9MHo4cLVqozm6yD2-V4ThS6WFrPwzOpoDtQIKwV0XyAyVzAwh6hp_SvCBMu9sZjVReyn5wldExz-zZPhpO_IdB8pvTb5AJusndoCHAAAAAUZFO8YA")
STRING5 = getenv("STRING_SESSION5", "AQAh8PeDJXY8BDRqpsOOxw5VXYbJjmk5YzHGEJWbufRml00m-tIEvLDNe5SiEDkahuW1f3_MRfMrl9IlUOGX_xfysNGgU5BJg47oB64FB32y7bED96L1ngcSMobZQmJ8Zd74eK0sIu6xhP3Uw4UcZcCs4e67DJr0jy37TfkdjlIvy0cKCfD_OH0GcRN_WQOePOAIFnf07xt_Q4Sb0AZreq6dF-k7vvxCI67aIwZQgmlY9V-bJoT-JjLc8XvRXnmsbzbs68sTVpL255PeaISzpujzpE0aB6-9TH1nw91JofS2Hj8Yz7BQ77q3p1AoOlysbaeJqcXv1A-TiXIzO18qE_vqAAAAAVQKjnUA")

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "nottyylogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/56d1760224589ee370186.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/56d1760224589ee370186.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "assets/Global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "assets/Stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "assets/Stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
