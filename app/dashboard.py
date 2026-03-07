import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Data Eng Project - Insights", layout="wide")

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = "127.0.0.1"
db_name = "student_wellbeing_db"
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:5432/{db_name}")

st.title("🚀 Student Productivity & Wellbeing Dashboard")
st.markdown("Dados integrados de **Tempo de Tela**, **Performance Acadêmica** e **Clima**.")

@st.cache_data
def get_data():
    return pd.read_sql("SELECT * FROM fact_student_performance", engine)

try:
    df = get_data()

    st.sidebar.header("Filtros")
    stress_filter = st.sidebar.multiselect("Nível de Estresse", options=df['stress_level'].unique(), default=df['stress_level'].unique())
    df_filtered = df[df['stress_level'].isin(stress_filter)]

    c1, c2, c3 = st.columns(3)
    c1.metric("Estudantes Analisados", len(df_filtered))
    c2.metric("Média Score Acadêmico", f"{df_filtered['exam_score'].mean():.2f}")
    c3.metric("Tempo Médio de Tela (h)", f"{df_filtered['daily_phone_hours'].mean():.1f}h")

    st.subheader("Relação: Tempo de Celular vs. Performance")
    st.scatter_chart(data=df_filtered, x='daily_phone_hours', y='exam_score', color='stress_level')

    st.write("### Tabela de Dados (Top 10)")
    st.dataframe(df_filtered.head(10))

except Exception as e:
    st.error(f"Erro ao carregar dashboard: {e}")