# Demographic Data Analyzer

import pandas as pd
import numpy as np

df = pd.read_csv('P2/adult.data.csv')


print(df.head())
print(df.describe())
print(df.info())

#1 How many people of each race are represented in this dataset?

race_counts = df['race'].value_counts()
print(race_counts)

#2 What is the average age of men?

average_age = df[df['sex'] == "Male"]['age'].mean()
print(average_age)

#3 What is the percentage of people who have a Bachelor's degree?

value_bachelors = df[df['education'] == 'Bachelors']['education-num'].count()
total_people = df['education'].count()
percentage_bachelors = (value_bachelors/total_people)*100
print(percentage_bachelors)

#4 What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

advanced_education_salary = df[df['education'].isin(['Bachelors','Masters', 'Doctorate'])]['salary'] == '>50K'
advanced_education = df[df['education'].isin(['Bachelors','Masters', 'Doctorate'])].count()
percentage_salary= advanced_education_salary/advanced_education * 100
print(percentage_salary)


