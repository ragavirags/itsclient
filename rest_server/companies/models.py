# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	open = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.ticker


class House(models.Model):
	lat=models.FloatField()
	lon=models.FloatField()
	income= models.FloatField()
	noofmem = models.FloatField()
	doorno= models.CharField(max_length=40,unique=True)
	def __str__(self):
		return str(self.doorno)

class Household(models.Model):
	name=models.CharField(max_length=40)
	gender=models.CharField(max_length=7)
	age=models.IntegerField()
	house=models.ForeignKey(House,on_delete=models.CASCADE)
	def __str__(self):
			return self.name

class Housephoto(models.Model):
	photo = models.FileField(null=True, blank= True)
	house=models.ForeignKey(House,on_delete=models.CASCADE)
	def __str__ (self):
		return str(self.house)

class Houseaudio(models.Model):
	audio = models.CharField(max_length=400)
	house=models.ForeignKey(House,on_delete=models.CASCADE)
	def __str__ (self):
		return self.audio

class Housevideo(models.Model):
	video = models.CharField(max_length=400)
	house=models.ForeignKey(House,on_delete=models.CASCADE)
	def __str__ (self):
		return self.video


class Farm(models.Model):
	area = models.FloatField()
	house=models.ForeignKey(House,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.house)

class Farmlocation(models.Model):
	lat=models.FloatField()
	lon=models.FloatField()
	farm= models.ForeignKey(Farm,on_delete=models.CASCADE)
	sequeneno=models.IntegerField()
	def __str__(self):
		return str(self.farm)

	season=models.CharField(max_length=345,unique=True)
class Crop(models.Model):
	farm= models.ForeignKey(Farm,on_delete=models.CASCADE)
	
	crop=models.CharField(max_length=345,unique=True)
	def __str__(self):
		return self.crop

class Season(models.Model):
	def __str__(self):
		return self.season

class Cropping(models.Model):
	farm=models.ForeignKey(Farm,on_delete=models.CASCADE)
	season=models.CharField(max_length=345,unique=False)
	year=models.CharField(max_length=400)
	paddypercent=models.FloatField()
	wheatpercent=models.FloatField()
	maizepercent=models.FloatField()
	cornpercent=models.FloatField()
	canepercent=models.FloatField()
	spicespercent=models.FloatField()
	oilseedspercent=models.FloatField()
	def __str__(self):
		return str(self.farm)

class Farmphoto(models.Model):
	photo = models.CharField(max_length=400)
	farm=models.ForeignKey(Farm,on_delete=models.CASCADE)
	def __str__ (self):
		return self.photo



class Well(models.Model):
	lat=models.FloatField()
	lon=models.FloatField()
	depth=models.FloatField()
	averageWaterYield=models.FloatField()
	farm=models.ForeignKey(Farm,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.farm)

class Datetime(models.Model):
	date=models.CharField(max_length=50)
	well=models.ForeignKey(Well,on_delete=models.CASCADE)
	wateryield=models.FloatField()
	def __str__(self):
		return str(self.well)

class Wellphoto(models.Model):
	photo=models.CharField(max_length=350)
	well=models.ForeignKey(Well,on_delete=models.CASCADE)
	def __str__(self):
		return self.photo
