from django.db import models

class Data(models.Model):
    age = models.IntegerField(default=0)
    attrition = models.CharField(max_length=3) 
    business_travel = models. CharField(max_length=100)
    daily_rate = models.IntegerField()
    department = models.CharField(max_length=100)
    distance_from_home = models.DecimalField(decimal_places=2, max_digits=10)
    education = models.IntegerField()
    education_field = models.CharField(max_length=100)
    employee_count = models.IntegerField()
    employee_number = models.IntegerField()
    environment_satisfaction = models.IntegerField()
    gender = models.CharField(max_length=100)
    hourly_rate = models.IntegerField()
    job_involvement = models.IntegerField()
    job_level = models.IntegerField()
    job_role = models.CharField(max_length=100)
    job_satisfaction = models.IntegerField()
    marital_status = models.CharField(max_length=100)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_rate = models.IntegerField()
    num_companies_worked = models.IntegerField()
    is_over_18 = models.CharField(max_length=1)
    over_time = models.CharField(max_length=100)
    percent_salary_hike = models.IntegerField()
    performance_rating = models.IntegerField()
    relationship_satisfaction = models.IntegerField()
    standard_hours = models.IntegerField()
    stock_option_level = models.IntegerField()
    total_working_years = models.IntegerField()
    training_time_last_year = models.IntegerField()
    work_life_balance = models.IntegerField()
    years_at_company = models.IntegerField()
    years_in_current_role = models.IntegerField()
    years_since_last_promotion = models.IntegerField()
    years_with_current_manager = models.IntegerField()
    

class Statistics(models.Model):
    number_of_people = models.IntegerField()
    age = models.DecimalField(max_digits=10, decimal_places=2)
    distance_from_home = models.DecimalField(max_digits=10, decimal_places=2) 
    job_level = models.DecimalField(max_digits=10, decimal_places=2)
    job_satisfaction = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2) 
    performance_rating = models.DecimalField(max_digits=10, decimal_places=2)
    percent_salary_hike = models.DecimalField(max_digits=10, decimal_places=2)
    relationship_satisfaction = models.DecimalField(max_digits=10, decimal_places=2)
    total_working_years = models.DecimalField(max_digits=10, decimal_places=2) 
    work_life_balance = models.DecimalField(max_digits=10, decimal_places=2)
    years_in_current_role = models.DecimalField(max_digits=10, decimal_places=2)
    years_at_company = models.DecimalField(max_digits=10, decimal_places=2)
    years_with_current_manager = models.DecimalField(max_digits=10, decimal_places=2)


class Feature(models.Model):
    name = models.CharField(max_length=100)
    importance = models.DecimalField(max_digits=10, decimal_places=2)
