from distutils.debug import DEBUG
from skype_handler import SkypeHandler

import logging

if __name__ == "__main__":
    logging.basicConfig(level=DEBUG)
    logging.info("Starting application")
    skype_handler = SkypeHandler()
    skype_handler.loop()

# TODO:
# For each hour of the day
# Get latest grazzine post
# If was published < 1 hour ago, download pic
# Send pic to some channel (skype, teams, whatsapp)
