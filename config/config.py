import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "16201655"))
API_HASH = getenv("API_HASH", "440ba807d2cdf696ca498d441e2a6b29")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "2121214342:AAHzQBOLsqAlENXdfOYjNUJZ4ti54LUvuco")
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


STRING1 = getenv("STRING_SESSION", "AQBxnZfefNiXRTOyZyKUUT6OxSCMFw7o-Z7Na8CjSOik42ZSwlwATUccYwW_Omy6yzUyxBHVOKnX3pNUpBNJhYmnERg2gR9XauOwY8UHZKPo7ZqlCsnCTuNVI862mPKlS45yFLGfHyOqhS3f2X4rUxHTOcsWugDeFRzeerXEWRchZUsTZ6tGvpiU6f4n3n6BmDkwNF5zRqj_rDBVRGE239LH89hGG0-ZmruTsl-oVCDdYhT1JRxGZt8GB5khHCmk04ZDZegYZtBgiycVftA3vr-2jF1XHkEOV_o2ueEvl32Ed39WyrPO8PRMH92ChzSN4sEiaYrd2_vcPzKjkOa26XjcAAAAAU5ywukA")
STRING2 = getenv("STRING_SESSION2", "AQCwiB3geW4mkLmt3WSXsCYjT5EHAPQ3cTztB-1pto6BEZGTKYNvy6lvUJAtRs-lXo5sJmMaStclV6atGeh1Tg2YvE_w1vlLZZInohWE61KsbsrMnSuzQrcMwwQLPfipkiI4BSrouI70YoP3aeGOBGePffJcjBOLBn5TLwIqGfOPCICdUft4WedWcs2ALN5UKChItJTUFrNZLoGVqD8gABlzXa9UEYnC4wg9OJ7dRx7cMAtwTtoY8zWoomHAzveijSqwp7e8CxAsUYSAKfpVYXtxcplzIhXFuofw7qDDU1nK--FF0VcfUOuUL3s-U_OU2waUJ9xBUo69Q5HkLsPRVGiZAAAAAVIu2WgA")
STRING3 = getenv("STRING_SESSION3", "AQAahm4_1zW_qL5rXvOVKMBaHcLrcfv-BSBbaJ_wbjxHYfFoSYTAoTpzS9B8QELiT6FWXdhDfUPNmaTriBaRQ9DaUCMT3cQfMUcU6GEW-5-XSOr4f6rDrFBCqKF252KCGLI1kGxi0FccIVM-dwB0HGgJ9mWQFYQPYi9iewZhYmymPUHHDNbEF8lAwMA8KOIlCAgUAszdXX1BMkrGOd_x3SnecihfCvoPyCOvQYvFFjucMm9MKOiWdV4nwHiyq9ZDwI04nLZMJMJ6WLJaREzFpk0cwD9a9-wh37A0RpyzQz1z4BRYzCKcFOuqcLmhMEv3MLIfM09tEFfe6I4cP7GUxbJdAAAAAVUGtKUA")
STRING4 = getenv("STRING_SESSION4", "AQCIZQQ0zXQkVXFP8NQNkAN1vGrtNKIMaZtkPfbpsmH4V9Hg85A7w2qg1ZhT883nBz8BowFMn6APQc2ylYmAvZq0ORbpxHDa-Ch8tdrJz-TcATB6cdyg4NSuyidjCT3Trb3sgmYI9FeaOxT9iw4xik9UiSn6Z9dQ5OmsjLUDlXZ1Itht3DFTqtMgqiM2zpQyKPbU406uR4RuQA-kPizMYYuuIfIk8NImdkhqN7qELqdf1BnJXinfi-Uxu-O_esNp68K3tVE3aqD1iieDjnK6yZBMpt7pKTzrH3HXtOwklSwQlxu7KYJ5Mby0AxjIANyBC6VFPCJ55WFilMjNOsZlsfIZAAAAAUZFO8YA")
STRING5 = getenv("STRING_SESSION5", "AQAXqzXaKPVoRTe_DD_aqavq4MsZkjFAmL-MuZJ2qkQ21sDIaCXuJY1dt3bo4G6iZqB6Zl-pSspyQ0iTz_kRnwfRFQcIv6Eob5l0I5ELtDqVL6q497blnRiBEww36T6QNlTddSAz6sKpOcMD9Phlj7HCUmvkFaLtlMTGt6V5Yt_2kPkXVNJoxdVRtOyc1mahvBU1S7aN-f6jH3yIm-eZz0kjWlabHi-zuXkCz-VdjNva9-3tpq6slff7S6DTaQPq3aP2YP-MkEzWqeMRf0KfauH0qiwxKzfNmK323T8-APQyTjpqYmrcOdVUPJX8F_HlQLJJtYZ1J3dZMdrJsqLzWc8RAAAAAVQKjnUA")

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
