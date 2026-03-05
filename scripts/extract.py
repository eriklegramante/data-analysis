import pandas as pd
import requests
import os

class DataExtractor:
    def __init__(self, api_key_env_var):
        self.api_key = os.getenv(api_key_env_var)
        if not self.api_key:
            raise ValueError(f"API key not found in environment variable: {api_key_env_var}")
        self.dataset_path = "dataset/"

    def extract_csv(self, filename):
        full_path = os.path.join(self.dataset_path, filename)
        try:
            df = pd.read_csv(full_path)
            print(f"Successfully extracted data from {filename}")
            return df
        except Exception as e:
            print(f"Error reading CSV file {filename}: {e}")
            return None
        
    def fetch_weather(self, city="São Paulo"):
        url = "http://api.weatherapi.com/v1/current.json" 
        params = {"key": self.api_key, "q": city}
        try:
            response = requests.get(url, params=params) 
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
        
    def extract_all(self):
        return {
            "screen_time": self.extract_csv("screen_time.csv"),
            "student_performance": self.extract_csv("student_performance.csv"),
            "weather": self.fetch_weather()
        }