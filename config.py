# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("23939637", ""))
API_HASH = getenv("477f51720ede3eef6997dbc442151c43", "")
BOT_TOKEN = getenv("8037285069:AAEnMzm90nfVSvJJmTrB_QGz1KD_K99zZ6c", "")
OWNER_ID = list(map(int, getenv("6425525488", "").split()))
MONGO_DB = getenv("mongodb+srv://hepoda3624:lA8B88ten9lJFTqu@cluster0.ymnbbuh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
LOG_GROUP = getenv("-4686512840", "")
CHANNEL_ID = int(getenv("-1002557248555", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
