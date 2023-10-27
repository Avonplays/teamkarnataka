import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "˹ᴧɢσꝛᴧ ꭙ ꝛσʙσᴛ˼")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6181817811").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamAgora/agoraxmusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Main_Crunch_Roll_India_Hindi")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/anime_universe_666)

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1800000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "54000000")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/243e34b03c4c12d07e100.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/778ad6f4d8530d226dfaa.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/03b3c5bb1149003e3d02c.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/f641ca2f977378dccd7fd.jpg"

STATS_IMG_URL = "https://telegra.ph/file/bd378c5ecf35dd6740931.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/2fe6ccd9bf66d57d0d76f.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/55c35846588ccd342b3e4.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/cbe0adf2d57159d134fe4.png"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d27397ccf6a2bdc9c18c0.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/3792b43eaf7fe50673064.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/124494e8462b062297911.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/685d379d4e8fee23d07b9.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/f4609e4a716fdd68d21bf.jpg"


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
            PING_IMG_URL = "https://te.legra.ph/file/bfb034cc44a595bc2efe0.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/19effe725dd12a4159b6b.jpg"
