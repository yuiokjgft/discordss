import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = "1138315374:AAFPSkDXI_OII2yed2OFXkkX6HjGijs1tc0"
    DATABASE_URL = "postgres://hndqyyxnzzmmko:30ae880ddd9628be40f9de042fe58ac66c253234ff6306b4a139d4a2871aae75@ec2-54-146-4-66.compute-1.amazonaws.com:5432/dbks5ngupfd278"
    APP_ID = "1948374"
    API_HASH = "113be69e13bf6f71583fb0783b1ab841"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "**rusak**"
      ]

      START_MSG = "**p [{}](tg://user?id={})**\n__rusak"
