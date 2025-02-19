from src.data_preprocessing import load_data, clean_data, merge_data
from src.eda import plot_rainfall_vs_yield, plot_temp_vs_yield, plot_co2_vs_yield
from src.time_series import decompose_time_series, forecast_temperature
from src.machine_learning import train_linear_regression, train_random_forest

# Load data
rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data = load_data()

# Clean data
rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data = clean_data(rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data)

# Merge datasets
merged_data = merge_data([rainfall_data, temperature_data, co2_data, food_prices_data, crop_yield_data])

# Exploratory Data Analysis (Plots)
plot_rainfall_vs_yield(merged_data)
plot_temp_vs_yield(merged_data)
plot_co2_vs_yield(merged_data)

# Time-Series Analysis (Decomposition & Forecast)
decompose_time_series(merged_data['Yield'])
forecast_temperature(merged_data['ANNUAL_y'])

# Machine Learning Models (Train and Evaluate)
train_linear_regression(merged_data)
train_random_forest(merged_data)
