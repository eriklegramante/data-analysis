import os
from sqlalchemy import create_engine

class DataLoader:
    def __init__(self):
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = "127.0.0.1"  
        port = "5432"
        db_name = "student_wellbeing_db"
        
        self.db_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
        self.engine = create_engine(self.db_url)

    def load_to_sql(self, df, table_name):
        try:
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
            print(f"Dados carregados no PostgreSQL com sucesso na tabela {table_name}")
        except Exception as e:
            print(f"Erro ao carregar no Postgres: {e}")