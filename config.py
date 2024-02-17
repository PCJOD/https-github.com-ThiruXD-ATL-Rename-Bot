import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21136840")
API_HASH = os.environ.get("API_HASH", "0f2ff6ef89fcd5ba226c3f40342f5319")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "pcott") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","pcrename4GBbot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","pcmoviegroup") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","pcott") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","jerinpc")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Pc4gb")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://Pc4gb:Pc4gb@cluster0.vu2mhmi.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/e1a2bef493178712d2785.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6719882299').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002113853127"))
