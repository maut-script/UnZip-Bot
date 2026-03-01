import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8488116365:AAEKUdp3AYmV0fnK-vzUs2cxLko9U0Pa0D4")
    API_ID = int(os.environ.get("API_ID","31879900" ))
    API_HASH = os.environ.get("API_HASH", "3238af8628b9134484a19cca430a962c")
    MAX_FILE_SIZE = 2194304000
    
    
