import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA

def decompose_time_series(crop_yield_ts):
    decomposition = seasonal_decompose(crop_yield_ts, model='additive', period=1)
    decomposition.plot()
    plt.savefig('outputs/plots/crop_yield_decomposition.png')
    plt.show()

def forecast_temperature(temperature_ts):
    model = ARIMA(temperature_ts, order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)
    print(f'Forecasted Temperatures: {forecast}')
