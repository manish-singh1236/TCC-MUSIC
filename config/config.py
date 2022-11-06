import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16201655"))
API_HASH = getenv("API_HASH", "440ba807d2cdf696ca498d441e2a6b29")
BOT_TOKEN = getenv("BOT_TOKEN", "2121214342:AAGMlHLIwcK2cV-tb0kCi9npuT7tahZaqb4")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Devarora0987:#Dev12345@cluster0.razivtc.mongodb.net/?retryWrites=true&w=majority")
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


STRING1 = getenv("STRING_SESSION", "AQAzApcTTmgEu-PMjw7PAvFVWUrLPFg0jqHAnmpbGi6hMetPmXHOz1O0_9ivOLP0Mfp6-oFDuomoTZA7EmP08dV6bR0mHS1UjHjrjn9S004m1L6IJNID8bBzlFTKLk_l-tO-drokbW3q4Sr1AhXQHZbqX70KQnKz0IqsYn2wxga0jwJ1nb3e9-XOwxI2Hna9iI9bSwAKgM5raRoJyQaEIqAfzTEOVft00PycuCehT5DPFDd6OrinzgsOMloVTDvDQkGCbEeiFbCA4naqlDed646PQ_o_FYybVHMRJPJRpsE8ohHZJh85d8Om87FFsuHImImJRUY7T-OGqqo26F_R7pt4AAAAAVQKjnUA")
STRING2 = getenv("STRING_SESSION2", "AQCFUgulvrKZ6Y_NM57QTNn3xMxWklTHJe2EiTVnM9-jgweeJycYHZjnrM8p4a8Hgu0pD2nrGarkXeY_f5xf_360V7KRTgh7vxL4_IK9PbPdKiRHcEaCwvaL6gUeswgvGj2j0RQ8upzM6hL_r8XsY3TTQIAvvfx3Z7AimR0nySO99_U7v7vlz4nM4fPrSrpj816Kd1fHD_862HMCC0hEgy-j0MRUlOMNPm2DhtwWonzNlnFOq4shWkIw_-JhdEaojXCMu-o5TQBHP1Bz2lIaprJyQEOOQc_kXLksUxpCQLEtzRzpblmHHXmWa8d81GU7SKhQAsjYfzj6XGp6xhxIL-MrAAAAAUZFO8YA")
STRING3 = getenv("STRING_SESSION3", "AQClBhxMfvwlf4Qk1CJgGx9yiCIJT3M16wc1Mb8N4qW80ZiF9HmXc5VsK_8nNx2p4IVdtEKHROOgP0k4EvoVCiaOdbekVOn2z2Vc69q6iy3eOgpSaKAsg4sW_3oRBtb9rrfi2uhFGqWSlpN6aCUIitGGTpKVRwO9U5vBzzbAMF2wv357WC2x-z62evvm_lzsFBI-uTljJ09zY4rXp6IDrMtdoYFFXkKWsXiutnIkOZ2pC_RlacCkD0mnX-5c5egVGQ8O0axZuZ08fZuV04ED7WUOIOaxtwrm2p8MSXlW4Ap5joJy6r9YzKvcRGJ6ING10oTtnV2H9S_pj7K1lQOpJ0yWAAAAAVUGtKUA")
STRING4 = getenv("STRING_SESSION4", "AQA7lbxNIS322kBJVA5iLjma3PojVWgFeMfBygI8HqiclGy9dykYR1sRPqgssrMd6vZUETkIrumCNKGQb41iSVYuYK9AoLTrgHs4d_oAe0P4VvqcgFiAwtQaRwdnfAOA1utTSWWmr9nc-qwsxLogzIfnrjbQ0bHvgMqjv_gFfkkrnnI7g2z5qvmtNgGrdQzLvrXv1Cw_rtmItb-N6cSQGdKEaSsJx3HB1nzbdUQEiZ_FgjRC1LwYu2WbHw05xDIkqqxQWzsF8lsgqdlFLgBMSGUN7_CvqYl6Vr-pOESruBLf9YfIgBoLjJ_xPmZdNmkx1Lmm7hN8Eyvv_pJXu8haGzxyAAAAAVIu2WgA")
STRING5 = getenv("STRING_SESSION5", "AQAxNvjIIdp-PrYJXRY6HLnXF8nN-TirdIh5V2Fphc7Ne0t3lTDeYEeun0e-w2MSIPnj9MgcDXNL2Rh1fF1rmf2hQSyI8Xxw4coetnbIyW0EFys65aK7w69XQ-l45AQQ9sBHQsoapgHszt6kCAJE59rNmyerPC87rSCfAkvq7BrRg0LFHyXl1elgvMub9TBso51jqt8XW4Jc2HF3SHLVaaL8yaV4YJ0ArJSPgRn8e2zasfTGFrbJY8y4-MDHnAB5eHIp8Rh5KpH0wLuSFzA76WPP1Hc03_uvCLcM71Z9AbxBpA--LZkVvO86DPQ1fXIkmBdSTW3pyHlOt7cOxEnEZuXAAAAAAU5ywukA")

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
