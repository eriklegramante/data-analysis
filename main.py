from scripts.extract import DataExtractor
from scripts.transform import DataTransformer # Novo import
from dotenv import load_dotenv

load_dotenv()

def run_pipeline():
    print("Iniciando o Pipeline...")
    
    extractor = DataExtractor("API_KEY_WEATHER")
    transformer = DataTransformer() # Instanciando

    raw_data = extractor.extract_all()
    
    if raw_data["screen_time"] is not None and raw_data["student_performance"] is not None:
        print("Passo 2: Transformando e integrando dados...")
        
        weather_df = transformer.process_weather(raw_data["weather"])
        
        final_df = transformer.integrate_data(
            raw_data["screen_time"], 
            raw_data["student_performance"], 
            weather_df
        )
        
        print(f"Sucesso! Dataset final gerado com {final_df.shape[0]} linhas.")

if __name__ == "__main__":
    run_pipeline()