from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
import json
# Create your views here.
class SpotifyData(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        return Response("Please add a slug of your spotify id")

    def retrieve(self, request, pk=None):
        # https://accounts.spotify.com/en/authorize?client_id=fe655269e9fc4b529c6453b20dff05e6&response_type=code&redirect_uri=https:%2F%2Flocalhost%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09
        gigantic_test_object = """{
    "context": {
    "external_urls": {
        "spotify": "http://open.spotify.com/user/spotify/playlist/49znshcYJROspEqBoHg3Sv"
    },
    "href": "https://api.spotify.com/v1/users/spotify/playlists/49znshcYJROspEqBoHg3Sv",
    "type": "playlist",
    "uri": "spotify:user:spotify:playlist:49znshcYJROspEqBoHg3Sv"
},
"timestamp": 1490252122574,
"progress_ms": 44272,
"is_playing": true,
"currently_playing_type": "track",
"item": {
    "album": {
        "album_type": "album",
        "external_urls": {
            "spotify": "https://open.spotify.com/album/6TJmQnO44YE5BtTxH8pop1"
        },
        "href": "https://api.spotify.com/v1/albums/6TJmQnO44YE5BtTxH8pop1",
        "id": "6TJmQnO44YE5BtTxH8pop1",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/8e13218039f81b000553e25522a7f0d7a0600f2e",
                "width": 629
            },
            {
                "height": 300,
                "url": "https://i.scdn.co/image/8c1e066b5d1045038437d92815d49987f519e44f",
                "width": 295
            },
            {
                "height": 64,
                "url": "https://i.scdn.co/image/d49268a8fc0768084f4750cf1647709e89a27172",
                "width": 63
            }
        ],
        "name": "Hot Fuss",
        "type": "album",
        "uri": "spotify:album:6TJmQnO44YE5BtTxH8pop1"
    },
    "artists": [
        {
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/0C0XlULifJtAgn6ZNCW2eu"
            },
            "href": "https://api.spotify.com/v1/artists/0C0XlULifJtAgn6ZNCW2eu",
            "id": "0C0XlULifJtAgn6ZNCW2eu",
            "name": "The Killers",
            "type": "artist",
            "uri": "spotify:artist:0C0XlULifJtAgn6ZNCW2eu"
        }
    ],
    "available_markets": [
        "AD",
        "AR",
        "TW",
        "UY"
    ],
    "disc_number": 1,
    "duration_ms": 222075,
    "explicit": false,
    "external_ids": {
        "isrc": "USIR20400274"
    },
    "external_urls": {
        "spotify": "https://open.spotify.com/track/0eGsygTp906u18L0Oimnem"
    },
    "href": "https://api.spotify.com/v1/tracks/0eGsygTp906u18L0Oimnem",
    "id": "0eGsygTp906u18L0Oimnem",
    "name": "Mr. Brightside",
    "popularity": 0,
    "preview_url": "http://d318706lgtcm8e.cloudfront.net/mp3-preview/f454c8224828e21fa146af84916fd22cb89cedc6",
    "track_number": 2,
    "type": "track",
    "uri": "spotify:track:0eGsygTp906u18L0Oimnem"
    }
}"""
        return Response(json.loads(gigantic_test_object))
        # return Response(f"{pk}")