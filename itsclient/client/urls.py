from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from client import views

app_name = 'client'

urlpatterns= [
	#url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),


	url(r'^Viewstocks/$', views.Viewstocks.as_view(), name='stocks'),
	url(r'^Viewhouses/$', views.Viewhouses.as_view(), name= 'houses'),
	url(r'^Viewhouseholds/$', views.Viewhouseholds.as_view(), name= 'households'),
	url(r'^Viewhousephotos/$', views.Viewhousephotos.as_view(), name= 'housephotos'),
	url(r'^Viewhouseaudios/$', views.Viewhouseaudios.as_view(), name= 'houseaudios'),
	url(r'^Viewhousevideos/$', views.Viewhousevideos.as_view(), name= 'housevideos'),
	url(r'^Viewsfarms/$', views.Viewsfarms.as_view(), name= 'farms'),
	url(r'^Viewfarmlocations/$', views.Viewfarmlocations.as_view(), name= 'farmlocations'),
	url(r'^Viewcrops/$', views.Viewcrops.as_view(), name= 'crops'),
	url(r'^Viewseasons/$', views.Viewseasons.as_view(), name= 'seasons'),
	url(r'^Viewcroppings/$', views.Viewcroppings.as_view(), name= 'croppings'),
	url(r'^Viewfarmphotos/$', views.Viewfarmphotos.as_view(), name= 'farmphotos'),
	url(r'^Viewwells/$', views.Viewwells.as_view(), name= 'wells'),
	url(r'^Viewdatetimes/$', views.Viewdatetimes.as_view(), name= 'datetimes'),
	url(r'^Viewwellphotos/$', views.Viewwellphotos.as_view(), name= 'wellphotos'),
	url(r'^Housemap/$', views.housemap, name='housemap'),
	url(r'^Wellmap/$', views.wellmap, name='wellmap'),
	url(r'^Farmmap/$', views.farmmap, name='farmmap'),
	url(r'^Cropmap/$', views.cropmap, name='cropmap'),
    url(r'^map/$', views.rend, name='map'),
]
