import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def exploratory_analysis(input_file):
    # Load processed data
    traffic_data = pd.read_csv(input_file)

    # Convert 'date' to datetime and extract hour and day of the week
    traffic_data['date'] = pd.to_datetime(traffic_data['date'], dayfirst=True)
    traffic_data['hour'] = traffic_data['date'].dt.hour
    traffic_data['day_of_week'] = traffic_data['date'].dt.dayofweek

    # Calculate average speed by hour
    avg_speed_by_hour = traffic_data.groupby('hour')['speed'].mean()

    # Calculate average speed by day of the week
    avg_speed_by_day = traffic_data.groupby('day_of_week')['speed'].mean()

    # Calculate congestion hotspots (assuming congestion is defined by speed < threshold)
    congestion_threshold = 20  # Example threshold value
    congestion_data = traffic_data[traffic_data['speed'] < congestion_threshold]
    congestion_by_hour = congestion_data.groupby('hour').size()

    # Plot average speed by hour
    plt.figure(figsize=(10, 6))
    avg_speed_by_hour.plot(kind='line')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Speed')
    plt.title('Average Traffic Speed by Hour')
    plt.grid(True)
    plt.savefig("output/avg_speed_by_hour.png")

    # Plot average speed by day of the week
    plt.figure(figsize=(10, 6))
    avg_speed_by_day.plot(kind='bar')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Speed')
    plt.title('Average Traffic Speed by Day of the Week')
    plt.grid(True)
    plt.savefig("output/avg_speed_by_day.png")

    # Plot congestion by hour
    plt.figure(figsize=(10, 6))
    congestion_by_hour.plot(kind='bar')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Congestion Events')
    plt.title('Congestion Events by Hour')
    plt.grid(True)
    plt.savefig("output/congestion_by_hour.png")

    # Additional EDA: speed distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(traffic_data['speed'], bins=30, kde=True)
    plt.xlabel('Speed')
    plt.ylabel('Frequency')
    plt.title('Distribution of Traffic Speeds')
    plt.grid(True)
    plt.savefig("output/speed_distribution.png")

    # Additional EDA: scatter plot of speed vs. hour
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='hour', y='speed', data=traffic_data, alpha=0.1)
    plt.xlabel('Hour of the Day')
    plt.ylabel('Speed')
    plt.title('Speed vs. Hour')
    plt.grid(True)
    plt.savefig("output/speed_vs_hour.png")

    plt.show()

if __name__ == "__main__":
    exploratory_analysis("data/processed/cleaned_traffic_data.csv")


