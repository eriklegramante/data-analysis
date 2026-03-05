import pandas as pd

class DataTransformer:
    def __init__(self):
        pass

    def clean_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = (
            df.columns.str.strip()
            .str.lower()
            .str.replace(' ', '_')
            .str.replace('(', '')
            .str.replace(')', '')
        )
        return df

    def process_weather(self, weather_json):
        if not weather_json:
            return None
        
        weather_data = {
            "city": weather_json['location']['name'],
            "temp_c": weather_json['current']['temp_c'],
            "condition": weather_json['current']['condition']['text'],
            "humidity": weather_json['current']['humidity'],
            "last_updated": weather_json['current']['last_updated']
        }
        return pd.DataFrame([weather_data])

    def integrate_data(self, screen_df, student_df, weather_df):
        screen_df = self.clean_column_names(screen_df)
        student_df = self.clean_column_names(student_df)

        combined_df = pd.merge(screen_df, student_df, on='user_id', how='inner')

        if weather_df is not None:
            combined_df['current_temp'] = weather_df['temp_c'].iloc[0]
            combined_df['weather_condition'] = weather_df['condition'].iloc[0]

        return combined_df