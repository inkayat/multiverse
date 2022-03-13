
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from multiverse.statistics.feature_importance import get_importance
from .models import Data, Statistics, Feature
from .serializers import DataSerializer, FeatureSerializer, StatisticsSerializer
import pandas as pd

columns = ('age', 
           'distance_from_home', 
           'education', 
           'gender', 
           'hourl_rate', 
           'job_level', 
           'job_role', 
           'job_satisfaction', 
           'marital_status', 
           'monthly_income', 
           'performance_rating', 
           'totat_working_years', 
           'years_in_current_role', 
           'years_at_company',)


@api_view(['POST'])
def add_data(request):
    item = DataSerializer(data=request.data)
  
    if Data.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
@api_view()
def data_details(request, id):
    order = get_object_or_404(Data, pk=id)
    serializer = DataSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def last(request):
    data = Data.objects.last()
    serializer = DataSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)
 
@api_view(['GET', 'POST'])
def data_list(request):
    if request.method == "GET":
        queryset = Data.objects.all()
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#Stattistics
@api_view()
def compute_mean(request):
    queryset = Data.objects.values()
    df = pd.DataFrame(list(queryset))
    mean_age = df['age'].mean()
    mean_percent_salary_hike = df['percent_salary_hike'].mean()
    mean_distance_from_home = df['distance_from_home'].mean()
    mean_job_level = df['job_level'].mean()
    mean_job_satisfaction = df['job_satisfaction'].mean()
    mean_monthly_income = df['monthly_income'].mean()
    mean_performance_rating = df['performance_rating'].mean()
    mean_relationship_satisfaction = df['relationship_satisfaction'].mean()
    mean_total_working_years = df['total_working_years'].mean()
    mean_work_life_balance = df['work_life_balance'].mean()
    mean_years_in_current_role = df['years_in_current_role'].mean()
    mean_years_at_current_company = df['years_at_company'].mean()
    mean_years_with_current_manager = df['years_with_current_manager'].mean()
    calc = Statistics(number_of_people=df.size, 
                      age=mean_age,
                      distance_from_home=mean_distance_from_home,
                      job_level=mean_job_level,
                      job_satisfaction=mean_job_satisfaction,
                      monthly_income=mean_monthly_income,
                      performance_rating=mean_performance_rating,
                      percent_salary_hike=mean_percent_salary_hike,
                      relationship_satisfaction=mean_relationship_satisfaction,
                      total_working_years=mean_total_working_years,
                      work_life_balance=mean_work_life_balance,
                      years_in_current_role=mean_years_in_current_role,
                      years_at_company=mean_years_at_current_company,
                      years_with_current_manager=mean_years_with_current_manager)
    serializer = StatisticsSerializer(calc)
    return Response(serializer.data, status=status.HTTP_200_OK)
   
@api_view()
def feature_importance(request, order):
    queryset = Data.objects.values()
    df = pd.DataFrame(list(queryset))
    feature_importance = get_importance(df)
    top_n_items = {k:feature_importance[k] for k in list(feature_importance)[:10]}
    features = list(feature_importance)
    fimp = Feature(name=features[order-1], importance=top_n_items[features[order-1]])
    serializer = FeatureSerializer(fimp)
    return Response(serializer.data, status=status.HTTP_200_OK) 
    
    
@api_view()
def feature_importance_list(request):
    queryset = Data.objects.values()
    df = pd.DataFrame(list(queryset))
    feature_importance = get_importance(df)
    top_n_items = {k:feature_importance[k] for k in list(feature_importance)[:10]}
    features = list(feature_importance)
    fimp = [Feature(name=features[i], importance=top_n_items[features[i]]) for i in range(10)]
    serializer = FeatureSerializer(fimp, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)