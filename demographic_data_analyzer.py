import pandas as pd

# Load the dataset
data = pd.read_csv('path_to_your_dataset.csv')  # Update with the correct path to your dataset

def race_count(data):
    return data['race'].value_counts()
def average_age_men(data):
    return round(data[data['sex'] == 'Male']['age'].mean(), 1)

def percentage_bachelors(data):
    total_people = len(data)
    bachelors_count = len(data[data['education'] == 'Bachelors'])
    return round((bachelors_count / total_people) * 100, 1)
def percentage_high_earning_advanced_education(data):
    advanced_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_earners = advanced_education[advanced_education['salary'] == '>50K']
    return round((len(high_earners) / len(advanced_education)) * 100, 1)
def percentage_high_earning_no_advanced_education(data):
    no_advanced_education = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    high_earners = no_advanced_education[no_advanced_education['salary'] == '>50K']
    return round((len(high_earners) / len(no_advanced_education)) * 100, 1)

def minimum_hours_per_week(data):
    return data['hours-per-week'].min()

def percentage_min_hours_high_earning(data):
    min_hours = minimum_hours_per_week(data)
    min_hours_workers = data[data['hours-per-week'] == min_hours]
    high_earners = min_hours_workers[min_hours_workers['salary'] == '>50K']
    return round((len(high_earners) / len(min_hours_workers)) * 100, 1)

def highest_earning_country(data):
    countries = data['native-country'].unique()
    country_percentage = {}
    
    for country in countries:
        total_people = len(data[data['native-country'] == country])
        high_earners = len(data[(data['native-country'] == country) & (data['salary'] == '>50K')])
        country_percentage[country] = (high_earners / total_people) * 100 if total_people > 0 else 0
    
    highest_country = max(country_percentage, key=country_percentage.get)
    return highest_country, round(country_percentage[highest_country], 1)

def popular_occupation_high_earning_india(data):
    india_high_earners = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    return india_high_earners['occupation'].mode()[0]
if __name__ == "__main__":
    print("Race Count:\n", race_count(data))
    print("Average Age of Men:", average_age_men(data))
    print("Percentage of People with Bachelor's Degree:", percentage_bachelors(data))
    print("Percentage of People with Advanced Education earning >50K:", percentage_high_earning_advanced_education(data))
    print("Percentage of People without Advanced Education earning >50K:", percentage_high_earning_no_advanced_education(data))
    print("Minimum Hours per Week:", minimum_hours_per_week(data))
    print("Percentage of Minimum Hours Workers earning >50K:", percentage_min_hours_high_earning(data))
    highest_country, percentage = highest_earning_country(data)
    print(f"Country with highest percentage of >50K earners: {highest_country} ({percentage}%)")
    print("Most popular occupation for those earning >50K in India:", popular_occupation_high_earning_india(data))




