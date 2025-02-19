import pandas as pd

def load_data():
    rainfall_data = pd.read_csv('data/raw/rainfall.csv')
    temperature_data = pd.read_csv('data/raw/temperature.csv')
    co2_data = pd.read_csv('data/raw/co2_levels.csv')
    food_prices_data = pd.read_csv('data/raw/food_prices.csv', low_memory=False)
    crop_yield_data = pd.read_csv('data/raw/crop_yield.csv')
    return rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data

def clean_data(rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data):
    # Clean each dataset (handling missing values, data type conversions)
    rainfall_data['YEAR'] = rainfall_data['YEAR'].astype(int)
    temperature_data['YEAR'] = temperature_data['YEAR'].astype(int)
    co2_data['YEAR'] = co2_data['YEAR'].astype(int)
    
    # Handling the YEAR column for food_prices_data
    if 'DATE' in food_prices_data.columns:  # If there is a 'DATE' column
        food_prices_data['YEAR'] = pd.to_datetime(food_prices_data['DATE'], dayfirst=True).dt.year
    else:
        print("No 'DATE' column found in food_prices_data. Generating YEAR column manually.")
        # Generate YEAR column based on row index or logic based on the dataset
        food_prices_data['YEAR'] = range(2000, 2000 + len(food_prices_data))  # Adjust year range if necessary
    
    food_prices_data['YEAR'] = food_prices_data['YEAR'].astype(int)
    
    crop_yield_data['YEAR'] = crop_yield_data['YEAR'].astype(int)
    
    # Ensure 'State' column exists or adjust the column names as necessary
    # Renaming relevant columns to 'State'
    if 'SUBDIVISION' in rainfall_data.columns:
        rainfall_data.rename(columns={'SUBDIVISION': 'State'}, inplace=True)
    
    if 'admin1' in food_prices_data.columns:
        food_prices_data.rename(columns={'admin1': 'State'}, inplace=True)
    
    # If 'State' column is missing in temperature and CO2 data, handle them separately
    # For now, we will not use 'State' for merging these two.
    return rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data

def merge_data(data):
    # Merging data based on YEAR and State columns for the ones that have 'State'
    merged_data = pd.merge(data[0], data[1], on=['YEAR'], how='inner')  # temperature_data does not have 'State'
    merged_data = pd.merge(merged_data, data[2], on=['YEAR'], how='inner')  # co2_data does not have 'State'
    merged_data = pd.merge(merged_data, data[3], on=['YEAR', 'State'], how='inner')  # food_prices_data has 'State'
    merged_data = pd.merge(merged_data, data[4], on=['YEAR'], how='inner')  # crop_yield_data does not have 'State'
    return merged_data
