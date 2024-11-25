import pandas as pd 
from datetime import date
from pymongo import MongoClient




def salaryBucket(Salary):
    if Salary < 50000:
        return "A"
    elif Salary >= 50000 and Salary <= 100000:
        return "B"
    else:
        return "C"

def transform_data(df):
    # Step 1: Drop rows with missing 'EmployeeID' as you intended
    df_cleaned = df.dropna(subset=["EmployeeID"])

    # Step 2: Remove rows where 'Salary' contains non-numeric characters, then convert 'Salary' to numeric
    df_cleaned = df_cleaned[~df_cleaned['Salary'].astype(str).str.contains('[A-Za-z]', na=False)]
    df_cleaned['Salary'] = pd.to_numeric(df_cleaned['Salary'], errors='coerce')

    # Step 3: Convert 'BirthDate' to datetime, coercing invalid formats to NaT
    df_cleaned['BirthDate'] = pd.to_datetime(df_cleaned['BirthDate'], errors='coerce')

    # Step 4: Drop rows where 'BirthDate' conversion failed (i.e., rows with NaT)
    df_cleaned = df_cleaned.dropna(subset=['BirthDate'])

    df_cleaned.columns = df_cleaned.columns.str.strip()

    pattern = r'[^a-zA-Z\s]'

    df_cleaned['FirstName'] = df_cleaned['FirstName'].str.replace(pattern, '', regex=True).str.strip()
    df_cleaned['LastName'] = df_cleaned['LastName'].str.replace(pattern, '', regex=True).str.strip()


    df_cleaned['FullName'] = df_cleaned['FirstName'] +" " + df_cleaned['LastName']
    reference_date = pd.Timestamp('2023-01-01')

    df_cleaned['Age'] = (reference_date - df_cleaned['BirthDate']).dt.days // 365

    #Format the 'BirthDate' column as 'dd/mm/yyyy' (optional)

    df_cleaned['BirthDate'] = df_cleaned['BirthDate'].dt.strftime('%d/%m/%Y')


    #Categorize employees based on their Salaries 
    df_cleaned['SalaryBucket'] = df_cleaned['Salary'].apply(salaryBucket)

    df_cleaned = df_cleaned.drop(['FirstName','LastName','BirthDate'], axis =1)

