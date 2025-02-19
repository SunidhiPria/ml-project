import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def plot_rainfall_vs_yield(merged_data):
    # Ensure numerical values for plotting
    merged_data['ANNUAL_x'] = pd.to_numeric(merged_data['ANNUAL_x'], errors='coerce')
    merged_data['Yield'] = pd.to_numeric(merged_data['Yield'], errors='coerce')

    # Drop rows with NaN values in the necessary columns
    merged_data = merged_data.dropna(subset=['ANNUAL_x', 'Yield'])

    # Check if the data is loaded correctly
    print(merged_data.head())
    print(merged_data.columns)

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=merged_data, x='YEAR', y='ANNUAL_x', label='Rainfall')
    sns.lineplot(data=merged_data, x='YEAR', y='Yield', label='Crop Yield', color='orange')
    plt.title('Rainfall vs Crop Yield')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)  # Add gridlines for better visibility
    plt.savefig('outputs/plots/rainfall_vs_yield.png')
    plt.show()

def plot_temp_vs_yield(merged_data):
    # Ensure numerical values for plotting
    merged_data['ANNUAL_y'] = pd.to_numeric(merged_data['ANNUAL_y'], errors='coerce')
    merged_data['Yield'] = pd.to_numeric(merged_data['Yield'], errors='coerce')

    # Drop rows with NaN values in the necessary columns
    merged_data = merged_data.dropna(subset=['ANNUAL_y', 'Yield'])

    # Check if the data is loaded correctly
    print(merged_data.head())
    print(merged_data.columns)

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=merged_data, x='YEAR', y='ANNUAL_y', label='Temperature')
    sns.lineplot(data=merged_data, x='YEAR', y='Yield', label='Crop Yield', color='green')
    plt.title('Temperature vs Crop Yield')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)  # Add gridlines for better visibility
    plt.savefig('outputs/plots/temp_vs_yield.png')
    plt.show()

def plot_co2_vs_yield(merged_data):
    # Ensure numerical values for plotting
    merged_data['Carbon Dioxide (ppm)'] = pd.to_numeric(merged_data['Carbon Dioxide (ppm)'], errors='coerce')
    merged_data['Yield'] = pd.to_numeric(merged_data['Yield'], errors='coerce')

    # Drop rows with NaN values in the necessary columns
    merged_data = merged_data.dropna(subset=['Carbon Dioxide (ppm)', 'Yield'])

    # Check if the data is loaded correctly
    print(merged_data.head())
    print(merged_data.columns)


    plt.figure(figsize=(10, 6))
    sns.lineplot(data=merged_data, x='YEAR', y='Carbon Dioxide (ppm)', label='CO2 Level')
    sns.lineplot(data=merged_data, x='YEAR', y='Yield', label='Crop Yield', color='red')
    plt.title('CO2 Levels vs Crop Yield')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)  # Add gridlines for better visibility
    plt.savefig('outputs/plots/co2_vs_yield.png')
    plt.show()

    print("Merged Data Shape: ", merged_data.shape)
    print("Merged Data Columns: ", merged_data.columns)
    print("Sample of Merged Data: ", merged_data.head())

    

