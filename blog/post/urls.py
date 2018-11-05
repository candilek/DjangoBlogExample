from django.conf.urls import url

from .views import *
#bütün view'ler içe aktarıldı.

urlpatterns = [

    url(r'^index/$', post_index),   #r: regular experession; ^ işareti ile başlar ve $ işareti ile biter.
    url(r'^details/$',post_detail),
    url(r'^create/$',post_create),
    url(r'^update/$',post_update),
    url(r'^delete/$',post_delete),

]