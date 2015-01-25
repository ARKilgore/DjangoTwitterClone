from django.db import models

class Tweet(models.Model):
	text = models.CharField(max_length=140)
	date = models.DateTimeField('date published')
	name = models.CharField(max_length=12)
	def __unicode__ (self):
		return self.text 
	