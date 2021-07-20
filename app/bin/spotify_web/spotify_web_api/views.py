from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
class SpotifyData(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        return Response("Please add a slug of your spotify id")

    def retrieve(self, request, pk=None):
# https://accounts.spotify.com/en/authorize?client_id=fe655269e9fc4b529c6453b20dff05e6&response_type=code&redirect_uri=https:%2F%2Flocalhost%2Fcallback&scope=user-read-private%20user-read-email&state=34fFs29kd09
        return Response(f"{pk}")