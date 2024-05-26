import pandas as pd

def create_dashboard(cleaned_data_path, forecast_data_path):
    # Load cleaned data
    cleaned_data = pd.read_csv(cleaned_data_path)

    # Load forecast data
    forecast_data = pd.read_csv(forecast_data_path)

    # Merge cleaned data with forecast data for dashboard
    dashboard_data = pd.merge(cleaned_data, forecast_data, left_on='date', right_on='ds', how='left')

    # Calculate key metrics
    average_speed = cleaned_data['speed'].mean()
    total_congestion_events = (cleaned_data['speed'] < 20).sum()  # Example threshold for congestion

    print(f"Average Speed: {average_speed:.2f}")
    print(f"Total Congestion Events: {total_congestion_events}")

    # Save merged data for further analysis if needed
    dashboard_data.to_csv("data/processed/dashboard_data.csv", index=False)

    print("Dashboard data prepared.")

if __name__ == "__main__":
    create_dashboard("data/processed/cleaned_traffic_data.csv", "data/processed/forecast.csv")


