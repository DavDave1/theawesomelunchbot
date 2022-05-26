from distutils.debug import DEBUG
from skype_handler import SkypeHandler
from decouple import config

import logging

LOG_FILE = config("DATA_FOLDER") + "/lunch_bot.log"

if __name__ == "__main__":
    logging.basicConfig(filename=LOG_FILE, level=DEBUG)
    print("Starting application")
    skype_handler = SkypeHandler()
    skype_handler.loop()

# TODO:
# For each hour of the day
# Get latest grazzine post
# If was published < 1 hour ago, download pic
# Send pic to some channel (skype, teams, whatsapp)
