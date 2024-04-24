from django.conf import settings
from django.shortcuts import render

def media_url(request):
    return {'media_url': settings.MEDIA_URL}