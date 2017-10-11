# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response
from rest_framework.views import APIView
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from django.conf.urls import url
from rest_framework import status
from django.template import loader,RequestContext
#import requests
import urllib2
import json
import urllib


	#template= loader.get_template('client/houses.html')




	#context={"data1": data1, "data": data}

def rend(request):
	template= loader.get_template('client/houses.html')
	response= urllib2.urlopen("http://10.0.3.23:1111/houses/?format=json")
	data= json.load(response)
	response1= urllib2.urlopen("http://10.0.3.23:1111/households/?format=json")
	data1= json.load(response1)
	response2= urllib2.urlopen("http://10.0.3.23:1111/housephotos/?format=json")
	data2= json.load(response2)
	context={"data" : data , "data1" : data1 , "data2" : data2}
	return HttpResponse(template.render(context,request))

def farmmap(request):
	template= loader.get_template('client/farms.html')
	response= urllib2.urlopen("http://10.0.3.23:1111/farmlocations/?format=json")
	data= json.load(response)
	response1= urllib2.urlopen("http://10.0.3.23:1111/farms/?format=json")
	data1= json.load(response1)
	response2= urllib2.urlopen("http://10.0.3.23:1111/households/?format=json")
	data2= json.load(response2)
	response3= urllib2.urlopen("http://10.0.3.23:1111/croppings/?format=json")
	data3= json.load(response3)
	context={"data" : data ,"data1": data1, "data2":data2, "data3": data3}
	return HttpResponse(template.render(context,request))

def cropmap(request):
	template= loader.get_template('client/farmmap.html')
	response= urllib2.urlopen("http://10.0.3.23:1111/farmlocations/?format=json")
	data= json.load(response)
	response1= urllib2.urlopen("http://10.0.3.23:1111/farms/?format=json")
	data1= json.load(response1)
	response2= urllib2.urlopen("http://10.0.3.23:1111/households/?format=json")
	data2= json.load(response2)
	response3= urllib2.urlopen("http://10.0.3.23:1111/croppings/?format=json")
	data3= json.load(response3)
	context={"data" : data ,"data1": data1, "data2":data2, "data3": data3}
	return HttpResponse(template.render(context,request))

def wellmap(request):
	template= loader.get_template('client/wells.html')
	response= urllib2.urlopen("http://10.0.3.23:1111/wells/?format=json")
	data= json.load(response)
	response1= urllib2.urlopen("http://10.0.3.23:1111/farms/?format=json")
	data1= json.load(response1)
	response2= urllib2.urlopen("http://10.0.3.23:1111/households/?format=json")
	data2= json.load(response2)
	context={"data" : data, "data1": data1, "data2" : data2}
	return HttpResponse(template.render(context,request))

def housemap(request):
	template= loader.get_template('client/map.html')
	response= urllib2.urlopen("http://10.0.3.23:1110/houses/?format=json")
	data= json.load(response)
	response= urllib2.urlopen("http://10.0.3.23:1110/households/?format=json")
	data1= json.load(response)
	details=[]
	locationlist=[]
	for record in data:
		lat= record['lat']
		lon = record['lon']
		door= record['doorno']
		locationlist.append(lat)
		locationlist.append(lon)
		locationlist.append(int(door))
	for record1 in data1:
		house = record1['house']
		name = record1['name']
		gender = record1['gender']
		age = record1['age']
		income = record['income']
		details.append(str(name))
		details.append(str(gender))
		details.append(str(age))
		details.append(str(income))
		details.append(str(house))
	context={"lst":locationlist, "lst1": details}
	return HttpResponse(template.render(context,request))


class Viewstocks(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/stocks/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewhouses(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/houses/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewhouseholds(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/households/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewhousephotos(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/housephotos/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewhouseaudios(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/houseaudios/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewhousevideos(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/housevideos/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewsfarms(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/farms/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass


class Viewfarmlocations(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/farmlocations/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass


class Viewcrops(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/crops/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass


class Viewseasons(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/seasons/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewcroppings(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/croppings/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewfarmphotos(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/farmphotos/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewwells(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/wells/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass


class Viewdatetimes(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/datetimes/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass

class Viewwellphotos(APIView):
	def get(self, request):
		response= urllib2.urlopen("http://10.0.3.23:1110/wellphotos/?format=json")
		data= json.load(response)
		return Response(data)
	def post(self):
		pass
