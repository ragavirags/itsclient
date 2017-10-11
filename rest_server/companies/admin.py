# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Stock, House, Household, Housephoto,Houseaudio, Housevideo,Farm, Farmlocation, Crop, Season, Cropping, Farmphoto, Well, Datetime, Wellphoto

admin.site.register(Stock)
admin.site.register(House)
admin.site.register(Household)
admin.site.register(Housephoto)
admin.site.register(Houseaudio)
admin.site.register(Housevideo)
admin.site.register(Farm)
admin.site.register(Farmlocation)
admin.site.register(Crop)
admin.site.register(Season)
admin.site.register(Cropping)
admin.site.register(Farmphoto)
admin.site.register(Well)
admin.site.register(Datetime)
admin.site.register(Wellphoto)
