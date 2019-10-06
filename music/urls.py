from django.urls import path
from . import views
from django.conf.urls import include, url

app_name='music'
urlpatterns = [
    # /music/
    path('', views.index, name="index"),

    #/music/id
    # I learned params here
    path('<int:album_id>/', views.detail, name="detail")
]