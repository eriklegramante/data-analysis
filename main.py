from scripts.extract import DataExtractor
from scripts.transform import DataTransformer
from scripts.load import DataLoader  # Certifique-se de que este import existe!
from scripts.utils import setup_logging
from dotenv import load_dotenv

load_dotenv()

logger = setup_logging()

def run_pipeline():
    logger.info("--- INICIANDO PIPELINE DE DADOS ---")

    extractor = DataExtractor("API_KEY")
    transformer = DataTransformer()
    loader = DataLoader()

    logger.info("Passo 1: Extraindo dados de CSV e API...")
    raw_data = extractor.extract_all()

    if raw_data["screen_time"] is not None and raw_data["student_performance"] is not None:
        logger.info("Passo 2: Transformando e integrando dados...")
        
        weather_df = transformer.process_weather(raw_data["weather"])
        
        final_df = transformer.integrate_data(
            screen_df=raw_data["screen_time"], 
            student_df=raw_data["student_performance"], 
            weather_df=weather_df
        )

        if final_df is not None:
            logger.info(f"Sucesso! Dataset final gerado com {final_df.shape[0]} linhas.")
            logger.info("Passo 3: Carregando dados no banco de dados...")
            
            loader.load_to_sql(final_df, "fact_student_performance")
            
            logger.info("--- PIPELINE FINALIZADO COM SUCESSO ---")
        else:
            logger.error("Falha na integração: O DataFrame final está vazio (IDs não coincidem).")
    else:
        logger.error("Falha crítica: Não foi possível ler os arquivos CSV originais.")

if __name__ == "__main__":
    run_pipeline()