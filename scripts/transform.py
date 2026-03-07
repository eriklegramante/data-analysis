import pandas as pd

class DataTransformer:
    def __init__(self):
        pass

    def clean_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """Padroniza nomes de colunas para snake_case."""
        df.columns = (
            df.columns.str.strip()
            .str.lower()
            .str.replace(' ', '_')
            .str.replace('(', '')
            .str.replace(')', '')
        )
        return df

    def process_weather(self, weather_json):
        """Converte o JSON da API em um DataFrame de uma linha."""
        if not weather_json or 'current' not in weather_json:
            return None
        
        weather_data = {
            "temp_c": weather_json['current']['temp_c'],
            "condition": weather_json['current']['condition']['text'],
            "humidity": weather_json['current']['humidity']
        }
        return pd.DataFrame([weather_data])

    def integrate_data(self, screen_df, student_df, weather_df):
        screen_df = self.clean_column_names(screen_df)
        student_df = self.clean_column_names(student_df)

        student_df = student_df.rename(columns={'student_id': 'user_id'})

        screen_df['user_id'] = screen_df['user_id'].str.replace('U', '', case=False).str.strip()
        student_df['user_id'] = student_df['user_id'].astype(str).str.strip()
        
        cols_to_drop = ['age', 'gender', 'sleep_hours', 'social_media_hours']
        student_df = student_df.drop(columns=[c for c in cols_to_drop if c in student_df.columns])

        try:
            combined_df = pd.merge(screen_df, student_df, on='user_id', how='inner')
            
            if combined_df.empty:
                print("Aviso: O merge ainda resultou em vazio. Verifique se os números de ID existem em ambos os CSVs.")
                return None

            if weather_df is not None and not weather_df.empty:
                combined_df['env_temp_c'] = weather_df['temp_c'].iloc[0]
                combined_df['env_condition'] = weather_df['condition'].iloc[0]
            
            return combined_df

        except Exception as e:
            print(f"Erro fatal no Merge: {e}")
            return None