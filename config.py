import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22519172"))
API_HASH = getenv("API_HASH", "ffe9dd332d6e8efda845ad8e641a8ec1")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7121054769:AAHNgUmA6E5Bny2Z3R8rAqdrOUonwEGz2No")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://toxichina:toxichina@cluster0.reizw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Hina Music ✨")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1001392902114"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5195444280"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BrandrdXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/haxkx")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/haxkx_discussion")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION",  "BQFXnYQASsQfHyJSLTuzbGrzAAMm6aMbRsruDaUOichwUXKmIoBRA7M38xYmXe_mz_XxkUfzPa0Wj3LbjkC0hc5k2f9vnyEYso1_W37v0CChRPPTMJEZVva9tz4LWYAsMLWAE2GzNJ3q7VCI8K8SNUg9zMCpaNZSLJZ8H6rM_5-CfXDj51FTolt1FZfgRUl8g_lHpqLwwhh9Ddoz24gFxyO3YKubbGHJt23_sjeGR61OjyysKhM4tkvN3o2BwKEMGxvaHQyDQmYrX2jrgaOtAOxqVqEN5T0_rv0jA9iW-Wx0MJxgi-6D8EfRMF_LaRtJdQljfpVm3gOigJ-KanbOrU8O1lFdJQAAAAGKBGSZAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/7ab5ed9bfbbc5a060392e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/89cb23a04d6bb7c7a20ab.mp4"
)
PLAYLIST_IMG_URL = "https://graph.org/file/49379e9fe323b923a2dc4.jpg"
STATS_IMG_URL = "https://graph.org/file/709fdd164660d5add7b5f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/244e7569f41400dd0e024.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/851a9a173ea0bbe740e4c.jpg"
STREAM_IMG_URL = "https://graph.org/file/1a4e7f09f968d9207a291.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/8bd25e1b5fffb97ea343e.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/18ba535b174ac0649b23b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3434af0772e3ed4e4f27c.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/1bfce7a64228c69e43802.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/6e59e4dbcb74fec678d10.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
