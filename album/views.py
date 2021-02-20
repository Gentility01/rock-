from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def album(request):
    return render (request , 'album/album.html')
