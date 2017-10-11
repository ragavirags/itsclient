from rest_framework import serializers
from .models import Stock,  House, Household, Housephoto,Houseaudio, Housevideo,Farm, Farmlocation, Crop, Season, Cropping, Farmphoto,Well, Datetime, Wellphoto

class StockSerializer(serializers.ModelSerializer):

	class Meta:
		model = Stock
		#fields = ('ticker', 'volume')
		fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):

	class Meta:
		model = House
		fields = '__all__'

class HouseholdSerializer(serializers.ModelSerializer):

	class Meta:
		model = Household
		fields = '__all__'

class HousephotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Housephoto
		fields = '__all__'

class HouseaudioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Houseaudio
		fields = '__all__'

class HousevideoSerializer(serializers.ModelSerializer):

	class Meta:
		model =Housevideo
		fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):

	class Meta:
		model = Farm
		fields = '__all__'

class FarmlocationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Farmlocation
		fields = '__all__'

class CropSerializer(serializers.ModelSerializer):

	class Meta:
		model = Crop
		fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Season
		fields = '__all__'

class CroppingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cropping
		fields = '__all__'

class FarmphotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Farmphoto
		fields = '__all__'

class WellSerializer(serializers.ModelSerializer):

	class Meta:
		model = Well
		fields = '__all__'

class DatetimeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Datetime
		fields = '__all__'

class WellphotoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Wellphoto
		fields = '__all__'
