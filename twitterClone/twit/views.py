from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from twit.models import tweet

def index(request):
    return HttpResponse(Question.objects.all())
