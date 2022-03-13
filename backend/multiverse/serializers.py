from django.db.models import fields
from rest_framework import serializers
from .models import Data, Statistics, Feature
 
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        exclude = ('id',)
  
class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('name', 'importance',)