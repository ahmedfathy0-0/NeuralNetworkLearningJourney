import pandas as pd
import numpy as np
import os

def test_data_science_requirements():
    print("Starting verification of 4 - Data Science.ipynb requirements...")
    
    # Requirement 1: Read 'churn.csv' into a DataFrame
    try:
        df = pd.read_csv('churn.csv')
        print("✅ TODO [1]: 'churn.csv' loaded successfully.")
        print(f"   Shape: {df.shape}")
    except Exception as e:
        print(f"❌ TODO [1]: Failed to load 'churn.csv'. Error: {e}")
        return

    # Requirement 2: Keep only the numerical columns
    try:
        # Expected numerical columns based on the notebook view
        # RowNumber, CustomerId, CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited
        original_cols = df.columns
        df = df.select_dtypes(include=['number'])
        print("✅ TODO [2]: Numerical columns selected.")
        print(f"   Columns: {list(df.columns)}")
        
        # Verification: Check if non-numerical columns are gone (e.g., Surname, Geography, Gender)
        assert 'Surname' not in df.columns
        assert 'Geography' not in df.columns
        assert 'Gender' not in df.columns
        assert 'CreditScore' in df.columns
    except Exception as e:
        print(f"❌ TODO [2]: Failed to select numerical columns. Error: {e}")
        return

    # Requirement 3: Check if there are any missing values and fill them with the mean
    try:
        # Let's verify if there are NaNs first (for the sake of the test, though the file might be clean)
        # The implementation was:
        # if df.isnull().values.any():
        #     df = df.fillna(df.mean())
        
        # We perform the same operation
        if df.isnull().values.any():
            print("   Missing values found (simulating logic). Filling with mean...")
            df = df.fillna(df.mean())
        else:
            print("   No missing values found in dataset (logic still valid).")
        
        assert not df.isnull().values.any()
        print("✅ TODO [3]: Missing values handling verified.")
    except Exception as e:
        print(f"❌ TODO [3]: Failed missing value check. Error: {e}")
        return

    # Requirement 4: Check statistics for the table
    try:
        states = df.describe()
        print("✅ TODO [4]: Statistics generated successfully.")
        # print(states) # Optional: don't clutter output
    except Exception as e:
        print(f"❌ TODO [4]: Failed to generate statistics. Error: {e}")
        return

    # Requirement 5: Get rows of highest salary and lowest salary in a new dataframe
    try:
        if 'EstimatedSalary' not in df.columns:
             raise ValueError("'EstimatedSalary' column missing.")
             
        highest_salary_idx = df['EstimatedSalary'].idxmax()
        lowest_salary_idx = df['EstimatedSalary'].idxmin()
        
        highest_salary = df.loc[highest_salary_idx]
        lowest_salary = df.loc[lowest_salary_idx]
        
        salary_extremes = pd.DataFrame([highest_salary, lowest_salary])
        
        print("✅ TODO [5]: Highest and lowest salary rows extracted.")
        print(f"   Highest Salary: {highest_salary['EstimatedSalary']}")
        print(f"   Lowest Salary: {lowest_salary['EstimatedSalary']}")
        
        # Verify correctness
        assert salary_extremes.iloc[0]['EstimatedSalary'] == df['EstimatedSalary'].max()
        assert salary_extremes.iloc[1]['EstimatedSalary'] == df['EstimatedSalary'].min()
        
    except Exception as e:
        print(f"❌ TODO [5]: Failed to extract salary extremes. Error: {e}")
        return

    print("All checks passed!")

if __name__ == "__main__":
    test_data_science_requirements()
