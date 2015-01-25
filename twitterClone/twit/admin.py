from django.contrib import admin

# Register your models here.
from django.contrib import admin
from twit.models import Tweet

class TwitAdmin(admin.ModelAdmin):
	fields = ['text', 'date', 'name']

admin.site.register(Twit, TwitAdmin)
