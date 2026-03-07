import os
from sqlalchemy import create_engine

class DataLoader:
    def __init__(self):
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST") 
        port = os.getenv("POSTGRES_PORT", "5432")
        db_name = os.getenv("POSTGRES_DB", "postgres")
        
        self.db_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
        
        self.engine = create_engine(self.db_url, pool_pre_ping=True)

    def load_to_sql(self, df, table_name):
        try:
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
            print(f"✅ Sucesso! Dados carregados no Supabase na tabela: {table_name}")
        except Exception as e:
            print(f"❌ Erro ao carregar no Supabase: {e}")