import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16201655"))
API_HASH = getenv("API_HASH", "440ba807d2cdf696ca498d441e2a6b29")
BOT_TOKEN = getenv("BOT_TOKEN", "2121214342:AAHfGDnnv_QjqXRu1St7_P7yyPK3fASEQkA")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hnyx:mongo@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001853541618"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ғᴀʟʟᴇɴ2.0ダ ᴍᴜ𝕤ɪᴄ ダ𝕃𝕖𝕘𝕖𝕟𝕕​")
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5037053047").split())
)
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/FallenXBots")
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/FALLEN_BOT_SUPPORT")

DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "59006")
)

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "10998")
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

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "False")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/ll_ll_LegendHacker_IN_ll_ll")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "50"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)
TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2073741824")
)


STRING1 = getenv("STRING_SESSION", "BQA7Ur_9sQ482tLKkF-hkt58W_BYK1IoNC3DBPu-QOSC1TF-WTu0pCZ1s2fyp6glBmsF8FKxaAx9mpY37-dAPHAnlIolgmHF9kYPU11JdF5ZkmRG602XpAkASNbXqVKf6LUTiByu_S5-_T5itPIzj3u5wYSR2hDRdcNYDpbJMAPe0yEU60LnQ9Ibm8BbAaR5eib3-zwmnelvrWzkANpcQoaSKIjwBJFL-ldpjJcDsvrUILy62rzksIGlSUsQ5V3XxECsTzKhBj63g4249iM_aBij5udBGwYcD81eV0Gh7zmh70YJcxS6XbpSpXw1p3Efuonvi9sMEXA-yyRbUiR2dzeKAAAAAVG736kA")
STRING2 = getenv("STRING_SESSION2", "BQBT3rEnmq8fJ0IK4-3jSQL7AOxo76Ku19unsntxXGLpgdNc7-cdHfQw71bSZ9xCC12tRyY15MpHXohNiCqwrZkaG-8MpEzfHnGmqMe8A2pstyTz1bAAudzSgUneOUIg0TRQwMvGb6xXT7k6DbkC7q4_3YIAkgGzv0ntGrIvmAbVQWiEiyHAGsSX0cI2ZFp4dQb_THCQ5vRzqpdvL9ewaeEPDqUil4cWapACPUrRleqRDR_Ryd-6CZfVe_QQmpZ_KVELUFTD2M7J204NnMtcvVWXSa1Gp2e5xDfgF0uatH2tSDFMhZCo2_VejY7sIaXTJ9HLsCnVfLln83khWiu3_eE8AAAAAUp2YbgA")
STRING3 = getenv("STRING_SESSION3", "BQCctKHAAQ4t0QqBnYmXdCIh0hU-7hPETYExNxUbTuRsqmC4YI9KmUNd2gLq9ZvN9K-v_-kvO0yCJUPUmxDM-U8Zf006D3UIQt2nlzvXKgHWQrMvTt4APaZooeZ1ceFhe5iB5Lgu6CQv9W_7oSHc_1-E3hmY5niAMnU00Pi4kPvqRj0HhjSmIwdxKPiuWbJAOiGgRPngl-TiwPxWd6XFjjbzfGbkVVALaDoi9XVvUYhIAC-TBnVmKCYAkDWbpO2EmJwEwaTW_hSMU6aYlxqAGjhcyf6wJu1Hx35_RTqJ3iw9TYRhCW74mPxHLQy-4oYXkzZeYxAbQRQHP-R618ISTMocesNVgAA")
STRING4 = getenv("STRING_SESSION4", "BQBfOTMkWF845_OAmoN0R-9Kvdm1VI_N1VnBGvULO2zIX1y_GadMyE6cVwoa6T16z8_HmoxU1cek_UpLfsiy0emJQbaPbX_T7YtvkdGOul8oVinM11FlafTAw2QOveaeyZmdQQyLNjwvKGM5x1BBH8ZMARkl3RNZTQ9tukPk5s9Joygz1QY98T5GhdEmKi5j0JiAOFFBYKsbuf9kCQ77x6qwYaseuW5icEGdz3Lg7Y7VtbR2UTcnxnwWpggU9VGRiD_6I-dfU3EOeJMeK-FhqrZ670GtIZbY1x7cpKqSdMXlNuGKfpX_UNFcg9a-FFd2F885OHMcssGP_nD0qQl9EgKtAAAAAU8oNHsA")
STRING5 = getenv("STRING_SESSION5", "BQAqJAVDWV--B2yBXGOwWMLJw8313ap8YQ-OnZAe99LJ3iBK20iJR_fKGy6_N-LHajM4e0PdGlzSLVC6kc8KE2QKfmyGkQGtfx-9ui2Yy43Zgu_PRcBMtPkGQdHVnB3CLr9ob6d6WlPu7mDvKD1ZvPi3BohQ0b4xR8QmXq6fw5-n69v6eIcMBgeQiC-8r4zyuYdCXMCrjyLwerSZGlGCe6sVPkXUN97hy7JHEHDaWI80GCH0A3PJl363iHZPWsXdicVD6_tfvwLjZSDEuMjYGJ8DJCUjYHvkH9I-kFFeNZBrF2FcSX9eOXCCJ_9-OodaZvLL5d5uI6tLlYUDxQIUxxFrAAAAAVl0vC0A")

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "viruslogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/d9c4eca81a3d97696dd02.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "assets/Playlist.jpeg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://te.legra.ph/file/354711e8d255477308a2d.jpg",
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
    if GLOBAL_IMG_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
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
    if TELEGRAM_VIDEO_URL != "https://te.legra.ph/file/354711e8d255477308a2d.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()
