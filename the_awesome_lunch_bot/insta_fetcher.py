from instagrapi import Client
from decouple import config

import logging

INSTA_USERNAME = config("INSTA_USERNAME")
INSTA_PASSWORD = config("INSTA_PASSWORD")

client = Client()
client.login(INSTA_USERNAME, INSTA_PASSWORD)

grazzine_id = client.user_id_from_username("trattoriagrazzine")
latest_post = client.user_medias(grazzine_id, 1)[0]


class InstaFecther:
    client = Client()

    def __init__(self):
        client.login(INSTA_USERNAME, INSTA_PASSWORD)
        logging.info(f"insta fetcher logged in as {INSTA_USERNAME}")

    def fetch_menu(self, user):
        logging.info(f"fetching insta menu for {user}")
        user_id = self.client.user_id_from_username(user)
        latest = client.user_medias(user_id, 1)[0]

        return (latest.taken_at, f"https://instagram.com/p/{latest.code}")
