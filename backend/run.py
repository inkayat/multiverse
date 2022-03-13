import os 
import sys
import django
import pandas as pd

sys.path.append("/Users/tolga.inkaya/Desktop/multiverse/backend/")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "backend.settings")

django.setup()

#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from multiverse.models import Data

def run(): 
    print("reading data...")
    data_df = pd.read_csv("multiverse/data/data.csv")
    data_list = data_df.to_dict('records')
    for entry in data_list:
        data = Data(
                age = entry['Age'],
                attrition = entry['Attrition'],
                business_travel = entry['BusinessTravel'],
                daily_rate = entry['DailyRate'],
                department = entry['Department'],
                distance_from_home = entry["DistanceFromHome"],
                education = entry["Education"],
                education_field = entry["EducationField"],
                employee_count = entry["EmployeeCount"],
                employee_number = entry["EmployeeNumber"],
                environment_satisfaction = entry["EnvironmentSatisfaction"],
                gender = entry["Gender"],
                hourly_rate = entry["HourlyRate"],
                job_involvement = entry["JobInvolvement"],
                job_level = entry["JobLevel"],
                job_role = entry["JobRole"],
                job_satisfaction = entry["JobSatisfaction"],
                marital_status = entry["MaritalStatus"],
                monthly_income = entry["MonthlyIncome"],
                monthly_rate = entry["MonthlyRate"],
                num_companies_worked = entry["NumCompaniesWorked"],
                is_over_18 = entry["Over18"],
                over_time = entry["OverTime"],
                percent_salary_hike = entry["PercentSalaryHike"],
                performance_rating = entry["PerformanceRating"],
                relationship_satisfaction = entry["RelationshipSatisfaction"],
                standard_hours = entry["StandardHours"],
                stock_option_level = entry["StockOptionLevel"],
                total_working_years = entry["TotalWorkingYears"],
                training_time_last_year = entry["TrainingTimesLastYear"],
                work_life_balance = entry["WorkLifeBalance"],
                years_at_company = entry["YearsAtCompany"],
                years_in_current_role = entry["YearsInCurrentRole"],
                years_since_last_promotion = entry["YearsSinceLastPromotion"],
                years_with_current_manager = entry["YearsWithCurrManager"],
            )
        data.save()
    print("All entries saved into database")


if __name__ == "__main__":
    run()
