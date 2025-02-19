from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def train_linear_regression(merged_data):
    # Select relevant features (Rainfall, Temperature, CO2)
    X = merged_data[['ANNUAL_x', 'ANNUAL_y', 'Carbon Dioxide (ppm)']]
    y = merged_data['Yield']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error (Linear Regression): {mse}')

def train_random_forest(merged_data):
    X = merged_data[['ANNUAL_x', 'ANNUAL_y', 'Carbon Dioxide (ppm)']]
    y = merged_data['Yield']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf_model = RandomForestRegressor(n_estimators=100)
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    
    mse_rf = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error (Random Forest): {mse_rf}')
