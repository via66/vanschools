import csv
import urllib2
import time
from datetime import datetime
from datadisplay.models import Animal
from datadisplay.models import School

class csvParser:
   def __init__(self):
   	print "hello"
      	
   def parseAnimal(self, url):
      f = urllib2.urlopen(url)
      reader = csv.reader(f)
      reader.next()
      for row in reader:
      	new_animal = Animal(
      		date_lost = datetime.strptime(row[0],"%Y-%m-%d"),
      		color = row[1],
      		breed = row[2],
      		sex = row[3],
      		state = row[4],
      		name = row[5]
      		)
      	new_animal.save()
      	
   def parseSchool(self, url):
      f = urllib2.urlopen(url)
      reader = csv.reader(f)
      reader.next()
      for row in reader:
      	new_school = School(
      		name = unicode(row[0],"ISO-8859-1"),
      		latitude = float(row[1]),
      		longitude = float(row[2])
      		)
      	new_school.save()   	