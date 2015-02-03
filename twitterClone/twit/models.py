from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.conf import settings
from django.forms import ModelForm
from django.contrib.auth.models import User

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    date = models.DateTimeField('date published')
    name = models.CharField(max_length=12)
    def __unicode__ (self):
        return self.text

'''class SiteUser(AbstractBaseUser):
    email = models.EmailField('email address', max_length=200, unique=True, error_messages={'unique':'A user with this email already exists',}, help_text='Email Address')
    username = models.CharField(max_length=100,unique=True,error_messages={'unique':'Username is taken',},help_text='Username')
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.username'''