from django.conf import settings
import requests


class Spot_Wrap():
    def __init__(self, spotify_key):
        self.request = requests.Session()
        self.headers = {"Authorization":f"Bearer: {spotify_key}"}