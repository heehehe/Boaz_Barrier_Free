from django.db import models
import pandas as pd

# Create your models here.
class Facility(models.Model):
	대분류 = models.CharField(max_length=100, blank=True)
	소분류 = models.CharField(max_length=100, blank=True)
	시설명 = models.CharField(max_length=1000, blank=True)
	주소 = models.CharField(max_length=2000, blank=True)
	위도 = models.FloatField(blank=True)
	경도 = models.FloatField(blank=True)
	전화번호 = models.CharField(max_length=30, blank=True)
