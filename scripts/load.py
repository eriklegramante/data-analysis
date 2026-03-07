import os
from sqlalchemy import create_engine

class DataLoader:
    def __init__(self):
        self.db_url = "sqlite:///student_wellbeing.db"
        self.engine = create_engine(self.db_url)

    def load_to_sql(self, df, table_name):
        try:
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
            print(f"✅ Sucesso! Dados salvos no SQLite (student_wellbeing.db)")
        except Exception as e:
            print(f"❌ Erro ao salvar no SQLite: {e}")