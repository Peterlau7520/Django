from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album




def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums
    }
    # render returns a built it HttpResponse function
    return render(request, 'music/index.html', context)



def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
