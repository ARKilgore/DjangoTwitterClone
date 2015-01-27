from django.shortcuts import render
from django.http import HttpResponse
from twit.models import Tweet
from django.utils import timezone
from django.template import RequestContext, loader



def index(request):
    #username = request.POST['username']
    '''
    t = Tweet(text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eu nisl vulputate, dapibus arcu a.",
        date=timezone.now(), name="James D.")
    t.save()
    '''
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
'''
def add(request, n_name, n_text):
        t = Tweet(text = n_text, date=timezone.now(), name=n_name)
        t.save()
        index(request)
'''