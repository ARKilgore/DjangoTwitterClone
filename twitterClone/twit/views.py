from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from twit.models import Tweet
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

def index(request):
    context = {}
    return render(request, 'twit/login.html', context)

def authorize(request):
    context = {}
    user = authenticate(username=request.POST.get('user_name',False), password=request.POST.get('password',False))
    if user is not None:
        login(request, user)
        context['user'] = username=request.POST.get('user_name',False)
        twit_list = Tweet.objects.order_by('-date')[:10]
        context = { 'twit_list' : twit_list }
        return render(request, 'twit/index.html', context)
    else:
        context['errors'] = 'Username or Password is incorrect. Try again'
        return render(request, 'twit/login.html', context)

def leave(request):
    context = {}
    logout(request)
    return render(request, 'twit/login.html', context)

def register(request):
    context = {}
    return render(request, 'twit/registration.html', context)

def signup(request):
    context = {}
    username=request.POST.get('Username',False)
    if User.objects.filter(username=request.POST.get('Username',False)).exists():
        context['errors'] = 'This username is taken'
        return render(request, 'twit/registration.html', context)
    context['username'] = request.POST.get('Username',False)
    if User.objects.filter(email=request.POST.get('Email',False)).exists():
        context['errors'] = 'A user with this email already exists'
        return render(request, 'twit/registration.html', context)
    context['email'] = request.POST.get('Email',False)
    pass1 = request.POST.get('Password',False)
    pass2 = request.POST.get('password2',False)
    if pass1 != pass2:
        context['errors'] = 'Passwords do not match'
        return render(request, 'twit/registration.html', context)
    user = User.objects.create_user(request.POST.get('Username',False), request.POST.get('Email',False), request.POST.get('Password',False))
    user.save()
    context = {}
    return render(request, 'twit/login.html', context)

'''def signup(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    if form.is_valid():
        context['form'] = form
        # Passwords don't match
        if form.cleaned_data['password'] != form.cleaned_data['retype_password']:
            context['errors'] = 'The passwords you entered do not match.'
            return render(request, 'twit/register.html', context)
        # A user already exists with this email
        if SiteUser.objects.filter(email=form.cleaned_data['email']).count():
            context['errors'] = 'A user already exists with this email.'
            return render(request, 'twit/register.html', context)
        email = form.cleaned_data['email']
        password = form.clean_retype_password()
        form.save()
        user = authenticate(email=email, password=password)
        login(request, user) # Log the user in
        return HttpResponseRedirect(reverse('index')) # Redirect them to the home page
    context['form'] = form
    return render(request, 'twit/register.html', context)
'''
def home(request):
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
        t = Tweet(text = request.POST.get('twit_text',False), date = timezone.now(), name=request.POST.get('twit_name',False))
        t.save()
        return HttpResponseRedirect('/twit/feed')

def add(request, n_name, n_text):
    t = Tweet(text = n_text, date=timezone.now(), name=n_name)
    t.save()
    index(request)
