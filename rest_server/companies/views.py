# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Stock, House, Household, Housephoto,Houseaudio, Housevideo,Farm, Farmlocation, Crop, Season, Cropping, Farmphoto, Well, Datetime, Wellphoto

from .serializers import StockSerializer, HouseSerializer, HouseholdSerializer, HousephotoSerializer,HouseaudioSerializer, HousevideoSerializer,FarmSerializer, FarmlocationSerializer, CropSerializer, SeasonSerializer, CroppingSerializer, FarmphotoSerializer, WellSerializer, DatetimeSerializer, WellphotoSerializer


class StockList(APIView):

	def get(self, request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class HouseList(APIView):

	def get(self, request):
		houses = House.objects.all()
		serializer = HouseSerializer(houses, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class HouseholdList(APIView):

	def get(self, request):
		households = Household.objects.all()
		serializer = HouseholdSerializer(households, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class HousephotoList(APIView):

	def get(self, request):
		housephotos = Housephoto.objects.all()
		serializer = HousephotoSerializer(housephotos, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class HouseaudioList(APIView):

	def get(self, request):
		houseaudios = Houseaudio.objects.all()
		serializer = HouseaudioSerializer(houseaudios, many=True)
		return Response(serializer.data)

	def post(self):
		pass


class HousevideoList(APIView):

	def get(self, request):
		housevideos = Housevideo.objects.all()
		serializer = HousevideoSerializer(housevideos, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class FarmList(APIView):

	def get(self, request):
		farms = Farm.objects.all()
		serializer = FarmSerializer(farms, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class FarmlocationList(APIView):

	def get(self, request):
		farmlocations = Farmlocation.objects.all()
		serializer = FarmlocationSerializer(farmlocations, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class CropList(APIView):

	def get(self, request):
		crops = Crop.objects.all()
		serializer = cropSerializer(crops, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class SeasonList(APIView):

	def get(self, request):
		seasons = Season.objects.all()
		serializer = SeasonSerializer(seasons, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class CroppingList(APIView):

	def get(self, request):
		croppings = Cropping.objects.all()
		serializer = CroppingSerializer(croppings, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class FarmphotoList(APIView):

	def get(self, request):
		farmphotos = Framphoto.objects.all()
		serializer = FramphotoSerializer(farmphotos, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class WellList(APIView):

	def get(self, request):
		wells = Well.objects.all()
		serializer = WellSerializer(wells, many=True)
		return Response(serializer.data)

	def post(self):
		pass


class DatetimeList(APIView):

	def get(self, request):
		datetimes = Datetime.objects.all()
		serializer = DatetimeSerializer(datetimes, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class WellphotoList(APIView):

	def get(self, request):
		wellphotos = Wellphoto.objects.all()
		serializer = WellphotoSerializer(wellphotos, many=True)
		return Response(serializer.data)

	def post(self):
		pass
