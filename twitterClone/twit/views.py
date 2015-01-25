from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from twit.models import Tweet
from django.utils import timezone


def index(request):
    username = request.POST['username']
    t = Tweet(text="Wassup", date=timezone.now(), name="Reid")
    t.save()
    response = HttpResponse()
    for i in Tweet.objects.all():
        response.write("<br>")
        response.write(i.name + " said " + i.text + ": sent at ")
        response.write(i.date)
    return response