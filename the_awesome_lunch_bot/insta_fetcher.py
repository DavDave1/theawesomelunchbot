from instagrapi import Client
from decouple import config
from os.path import exists

import logging

INSTA_USERNAME = config("INSTA_USERNAME")
INSTA_PASSWORD = config("INSTA_PASSWORD")
INSTA_SETTINGS_PATH = config("DATA_FOLDER") + "/insta_settings.json"


class InstaFecther:
    client = Client()

    def __init__(self):
        if exists(INSTA_SETTINGS_PATH):
            self.client.load_settings(INSTA_SETTINGS_PATH)
        if self.client.login(INSTA_USERNAME, INSTA_PASSWORD):
            self.client.dump_settings(INSTA_SETTINGS_PATH)

        print(f"insta fetcher logged in as {INSTA_USERNAME}")

    def fetch_menu(self, user):
        print(f"fetching insta menu for {user}")
        user_id = self.client.user_id_from_username(user)
        latest = self.client.user_medias(user_id, 1)[0]

        return (latest.taken_at, f"https://instagram.com/p/{latest.code}")
