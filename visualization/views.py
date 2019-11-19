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
def home(request):
	fac_hospital = Facility.objects.filter(대분류='병원')
	fac_comforts = Facility.objects.filter(대분류='편의시설')
	fac_public = Facility.objects.filter(대분류='공공시설')
	fac_traffic = Facility.objects.filter(대분류='교통')
	args = {'fac_hospital': fac_hospital, 'fac_comforts': fac_comforts, 'fac_public': fac_public, 'fac_traffic': fac_traffic}
	return render(request, './home.html', args)

def facility_info(request):
	fac_hospital = Facility.objects.filter(대분류='병원')
	fac_comforts = Facility.objects.filter(대분류='편의시설')
	fac_public = Facility.objects.filter(대분류='공공시설')
	fac_traffic = Facility.objects.filter(대분류='교통')
	args = {'fac_hospital': fac_hospital, 'fac_comforts': fac_comforts, 'fac_public': fac_public, 'fac_traffic': fac_traffic}
	return render(request, './facility_info.html', args)