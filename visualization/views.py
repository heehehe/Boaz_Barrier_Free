from django.shortcuts import render
from .models import *
from visualization.models import *

# Create your views here.
'''
class HomeView(TemplateView):
	"""docstring for HomeView"""
	def get(self, request):
		대분류 = Facility.objects.all()
		args = {'대분류': 대분류}
		return render(request, './home.html', args)		


'''
def index(request):
	facility = Facility.objects.all()
	args = {'facility': facility}
	return render(request, './home.html', args)
