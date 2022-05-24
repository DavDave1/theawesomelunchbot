from sre_constants import IN_IGNORE
from instagrapi import Client
from decouple import config

INSTA_USERNAME = config("INSTA_USERNAME")
INSTA_PASSWORD = config("INSTA_PASSWORD")

client = Client()
client.login(INSTA_USERNAME, INSTA_PASSWORD)

grazzine_id = client.user_id_from_username("trattoriagrazzine")
latest_post = client.user_medias(grazzine_id, 1)[0]

print(f"{latest_post}")

# client.photo_download(latest_post.pk, "C:/code")

# TODO:
# For each hour of the day
# Get latest grazzine post
# If was published < 1 hour ago, download pic
# Send pic to some channel (skype, teams, whatsapp)
