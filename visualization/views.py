from django.shortcuts import render
from .models import *
from visualization.models import *
# from rest_framework import serializers

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
	fac_hospital = Facility.objects.filter(대분류='편의시설')
	# facility = serializers.serialize("json", facility)
	args = {'facility': facility, 'fac_hospital': fac_hospital}
	return render(request, './home.html', args)
