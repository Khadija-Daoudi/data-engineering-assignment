import pytest

import pandas as pd

import sys
import os

# Add the root directory of the project to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from scripts.transform import transform_data

def test_transform_data():
    # Example raw data
    data = pd.DataFrame({
        'EmployeeID': [1, 2],
        'FirstName': [' John ', 'Jane'],
        'LastName': ['Doe ', 'Smith'],
        'BirthDate': ['1990-01-01', '1985-06-15'],
        'Salary': [40000, 120000]
    })
    transformed = transform_data(data)

    # Validate the transformation
    assert 'FullName' in transformed.columns
    assert 'Age' in transformed.columns
    assert 'SalaryBucket' in transformed.columns
    assert transformed.iloc[0]['FullName'] == 'John Doe'
    assert transformed.iloc[1]['SalaryBucket'] == 'C'
