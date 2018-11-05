
from django.shortcuts import render, HttpResponse


def post_index (request):
    return HttpResponse("Burası post index sayfası!")

def post_detail (request):
    return HttpResponse("Burası post detail sayfası!")

def post_create(request):
    return HttpResponse("Burası post create sayfası!")

def post_update(request):
    return HttpResponse("Burası post update sayfası!")

def post_delete(request):
    return HttpResponse("Burası post delete sayfası!")








