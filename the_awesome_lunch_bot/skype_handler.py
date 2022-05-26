from skpy import SkypeEventLoop, SkypeNewMessageEvent
from decouple import config
import logging

from insta_fetcher import InstaFecther
from storage_connect import StorageConnect

USERNAME = config("SKYPE_USERNAME")
PASSWORD = config("SKYPE_PASSWORD")
SKYPE_TOKEN_KEY = "skype_token"
SKYPE_TOKEN_PATH = config("DATA_FOLDER") + "/skype_token.json"


class SkypeHandler(SkypeEventLoop):
    insta_fecther = InstaFecther()

    def __init__(self):
        storage = StorageConnect()

        if storage.connection.exists(SKYPE_TOKEN_KEY):
            token = storage.connection.get(SKYPE_TOKEN_KEY)

            with open(SKYPE_TOKEN_PATH, "w") as f:
                f.write(str(token))

        super(SkypeHandler, self).__init__(
            USERNAME, PASSWORD, SKYPE_TOKEN_PATH)

        with open(SKYPE_TOKEN_PATH, "r") as f:
            token = f.read()
            storage.connection.set(SKYPE_TOKEN_KEY, token)

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
