import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5032846789:AAGO5JMdzUT3xmboDZEqUHvgPhHCfcLWNlk")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 7469109))
    API_HASH = os.environ.get("v4d4023337b8cc46c306af69adb5fc21a")
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2118362497").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "postgres://hnfuntuvxhtdsa:8aa2d0e4b81e5d52c029aa351d52de3169627ef13d9b002f11dba08bd02f9ae3@ec2-54-198-213-75.compute-1.amazonaws.com:5432/d84mp878lr2f9g")

