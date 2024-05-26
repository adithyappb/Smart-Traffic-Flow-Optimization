from prophet import Prophet
import pandas as pd
from sklearn.metrics import mean_absolute_error

def time_series_forecasting(input_file):
    # Load data
    traffic_data = pd.read_csv(input_file)

    # Prepare data for Prophet
    traffic_data['ds'] = pd.to_datetime(traffic_data['date'], dayfirst=True)
    traffic_data['y'] = traffic_data['speed']
    prophet_data = traffic_data[['ds', 'y']]

    # Train Prophet model
    prophet_model = Prophet()
    prophet_model.fit(prophet_data)

    # Make predictions
    future = prophet_model.make_future_dataframe(periods=30)
    forecast = prophet_model.predict(future)

    # Evaluate model
    y_true = prophet_data['y']
    y_pred = forecast['yhat'][:len(y_true)]  # Align predictions with true values for comparison
    mae = mean_absolute_error(y_true, y_pred)
    print(f"Mean Absolute Error (MAE) of the model: {mae:.2f}")

    return forecast, mae

if __name__ == "__main__":
    forecast, mae = time_series_forecasting("data/processed/cleaned_traffic_data.csv")
    forecast.to_csv("data/processed/forecast.csv", index=False)


