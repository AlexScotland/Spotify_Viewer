from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request,'index.html')

def view_song(request):
    return render(request,'song_page.html')