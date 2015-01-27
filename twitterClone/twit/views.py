from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from twit.models import Tweet
from django.utils import timezone
from django.template import RequestContext, loader



def index(request):
    #username = request.POST['username']
    twit_list = Tweet.objects.order_by('-date')[:10]
    context = { 'twit_list' : twit_list }
    return render(request, 'twit/index.html', context)
    '''
        for i in Tweet.objects.all():
        response.write("<br>")
        response.write(i.name + " said " + i.text + ": sent at ")
        response.write(i.date)
        return response
    '''

def detail(request, twit_id):
    response = HttpResponse()
    count = 0;
    for i in Tweet.objects.all():
        response.write(i.text)
        response.write("<br>")
    return response

def tweet(request):
    t = Tweet(text=request.POST.get('twit_text', False), date = timezone.now(), name=request.POST.get('twit_name', False))
    t.save()
    t = Tweet(text='reid', date = timezone.now(), name='aaaaa')
    t.save()
    return HttpResponseRedirect('index')
'''
    def add(request, n_name, n_text):
    t = Tweet(text = n_text, date=timezone.now(), name=n_name)
    t.save()
    index(request)
'''