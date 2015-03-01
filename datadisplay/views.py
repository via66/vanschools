from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from datadisplay.models import School

def index(request):
	all_schools = School.objects.all()
	template = loader.get_template('datadisplay/index.html')
	context = RequestContext(request, {'allschools': all_schools,
		})
	return HttpResponse(template.render(context))
