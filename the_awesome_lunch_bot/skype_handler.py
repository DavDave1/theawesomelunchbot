from skpy import SkypeEventLoop, SkypeNewMessageEvent
from decouple import config
import logging

from insta_fetcher import InstaFecther

USERNAME = config("SKYPE_USERNAME")
PASSWORD = config("SKYPE_PASSWORD")


class SkypeHandler(SkypeEventLoop):
    insta_fecther = InstaFecther()

    def __init__(self):
        super(SkypeHandler, self).__init__(USERNAME, PASSWORD)
        logging.info(f"skype handler logged in as {USERNAME}")

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent) and not event.msg.userId == self.userId:
            match event.msg.content:
                case "!grazzine":
                    logging.info("got !grazzine command")
                    user = "trattoriagrazzine"
                    (timestamp, url) = self.insta_fecther.fetch_menu(
                        "trattoriagrazzine")
                    logging.info(f"menu fetched: {timestamp}, {url}")
                    event.msg.chat.sendMsg(
                        f"Ecco il menu di {user} del {timestamp}:\n\n{url}")
