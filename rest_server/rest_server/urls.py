"""rest_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from companies import views
#from client import views
#router=routers.DefaultRouter()
#router.register(r'Stock', views.StockList)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stocks/', views.StockList.as_view()),
    url(r'^houses/', views.HouseList.as_view()),
    url(r'^households/', views.HouseholdList.as_view()),
    url(r'^housephotos/', views.HousephotoList.as_view()),
    url(r'^houseaudios/', views.HouseaudioList.as_view()),
    url(r'^housevideos/', views.HousevideoList.as_view()),
    url(r'^farms/', views.FarmList.as_view()),
    url(r'^farmlocations/', views.FarmlocationList.as_view()),
    url(r'^crops/', views.CropList.as_view()),
    url(r'^seasons/', views.SeasonList.as_view()),
    url(r'^croppings/', views.CroppingList.as_view()),
    url(r'^farmphotos/', views.FarmphotoList.as_view()),
    url(r'^wells/', views.WellList.as_view()),
    url(r'^datetimes/', views.DatetimeList.as_view()),
    url(r'^wellphotos/', views.WellphotoList.as_view()),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    #url(r'^Viewstocks/', views.Viewstocks.as_view()),
    #url(r'^client/', include('client.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
