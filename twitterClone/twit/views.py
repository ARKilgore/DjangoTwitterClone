from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from twit.models import Tweet
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

'''def auth_login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    if form.is_valid() and 'email' in form.cleaned_data and 'password' in form.cleaned_data:
        user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))  # Redirect to homepage when the user logs in
        else:
            context['errors'] = 'Authentication failed.'
    context['form'] = form
    return render_to_response('twit/signin.html', context, context_instance=RequestContext(request))
'''

def index(request):
    return render(request, 'twit/registration.html')


def signup(request):
    user = User.objects.create_user(request.POST.get('Username',False), request.POST.get('Email',False), request.POST.get('Password',False))
    user.save()
    twit_list = Tweet.objects.order_by('-date')[:10]
    context = { 'twit_list' : twit_list }
    return render(request, 'twit/index.html', context)


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
        return HttpResponseRedirect('/twit')

def add(request, n_name, n_text):
    t = Tweet(text = n_text, date=timezone.now(), name=n_name)
    t.save()
    index(request)
