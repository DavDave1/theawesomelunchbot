from distutils.log import INFO
from skype_handler import SkypeHandler

import logging

if __name__ == "__main__":
    logging.basicConfig(filename="./data/lunch_bot.log", level=INFO)
    print("Starting application")
    skype_handler = SkypeHandler()
    skype_handler.loop()

# TODO:
# For each hour of the day
# Get latest grazzine post
# If was published < 1 hour ago, download pic
# Send pic to some channel (skype, teams, whatsapp)
