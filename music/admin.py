from django.contrib import admin

# Register your modelt s here.
from django.contrib import admin
from .models import Album, Song

admin.site.register(Album)
admin.site.register(Song)