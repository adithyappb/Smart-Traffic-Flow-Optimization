from pyspark.sql import SparkSession
import pandas as pd

def preprocess_data(input_path, output_path):
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("TrafficFlowPreprocessing") \
        .getOrCreate()

    # Load raw data
    traffic_data = spark.read.csv(input_path, header=True, inferSchema=True)

    # Data cleaning and preprocessing: filter out rows where speed <= 0
    cleaned_data = traffic_data.filter(traffic_data['speed'] > 0)

    # Collect the data to the driver node
    cleaned_data_pd = cleaned_data.toPandas()

    # Save processed data as a single CSV file
    cleaned_data_pd.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data("data/raw/traffic_data.csv", "data/processed/cleaned_traffic_data.csv")


