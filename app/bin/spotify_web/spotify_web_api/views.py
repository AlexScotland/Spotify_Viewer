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
        return Response(f"{pk}")