from django.shortcuts import render, redirect
from api.models import ShortLink

# Create your views here.
def redirect_user(request, short_code):
    shorten_link = ShortLink.objects.get(short_code=short_code)
    shorten_link.accessed += 1
    shorten_link.save()
    return redirect(shorten_link.original_link)