from instagrapi import Client
from decouple import config
from os.path import exists

from storage_connect import StorageConnect

import logging
import json

INSTA_USERNAME = config("INSTA_USERNAME")
INSTA_PASSWORD = config("INSTA_PASSWORD")
INSTA_SETTINGS_KEY = "insta_settings"


class InstaFecther:
    client = Client()
    storage = StorageConnect()

    def __init__(self):
        if self.storage.connection.exists(INSTA_SETTINGS_KEY):
            insta_settings = json.loads(
                self.storage.connection.get(INSTA_SETTINGS_KEY))

            self.client = Client(insta_settings)

        if self.client.login(INSTA_USERNAME, INSTA_PASSWORD):
            insta_settings = json.dumps(self.client.get_settings())
            self.storage.connection.set(INSTA_SETTINGS_KEY, insta_settings)

        print(f"insta fetcher logged in as {INSTA_USERNAME}")

    def fetch_menu(self, user):
        print(f"fetching insta menu for {user}")
        user_id = self.client.user_id_from_username(user)
        latest = self.client.user_medias(user_id, 1)[0]

        return (latest.taken_at, f"https://instagram.com/p/{latest.code}")
