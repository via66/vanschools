from django.db import models

# Create your models here.
class Animal(models.Model):
    date_lost = models.DateTimeField('date lost')
    color = models.CharField(max_length=20)
    breed = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    state = models.CharField(max_length=100)
    name = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name


class School(models.Model):
	latitude = models.FloatField(('Latitude'), blank=True, null=True)
	longitude = models.FloatField(('Longitude'), blank=True, null=True)
	name = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.name	