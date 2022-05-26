from skpy import SkypeEventLoop, SkypeNewMessageEvent
from decouple import config
import logging

from insta_fetcher import InstaFecther

USERNAME = config("SKYPE_USERNAME")
PASSWORD = config("SKYPE_PASSWORD")
SKYPE_TOKEN_KEY = "skype_token"


class SkypeHandler(SkypeEventLoop):
    insta_fecther = InstaFecther()

    def __init__(self):
        super(SkypeHandler, self).__init__(
            USERNAME, PASSWORD)
        print(f"skype handler logged in as {USERNAME}")

    def onEvent(self, event):
        if isinstance(event, SkypeNewMessageEvent) and not event.msg.userId == self.userId:
            match event.msg.content:
                case "!grazzine":
                    print("got !grazzine command")
                    user = "trattoriagrazzine"
                    (timestamp, url) = self.insta_fecther.fetch_menu(
                        "trattoriagrazzine")
                    print(f"menu fetched: {timestamp}, {url}")
                    event.msg.chat.sendMsg(
                        f"Ecco il menu di {user} del {timestamp}:\n\n{url}")
                case "!bip":
                    event.msg.chat.sendMsg("bop")
