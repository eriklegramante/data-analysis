import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

st.set_page_config(page_title="Student Data Insights", layout="wide", page_icon="📊")

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, '..', 'student_wellbeing.db')

engine = create_engine(f"sqlite:///{db_path}")

st.title("🚀 Student Productivity & Wellbeing Dashboard")
st.markdown("Dashboard alimentado por um **Pipeline de Dados End-to-End**.")

@st.cache_data
def get_data():
    return pd.read_sql("SELECT * FROM fact_student_performance", engine)

try:
    df = get_data()

    c1, c2, c3 = st.columns(3)
    c1.metric("Estudantes Analisados", f"{len(df):,}")
    c2.metric("Média Score Acadêmico", f"{df['exam_score'].mean():.2f}")
    c3.metric("Tempo Médio de Tela", f"{df['daily_phone_hours'].mean():.1f}h")

    st.sidebar.header("🔍 Filtros Analíticos")
    stress_levels = sorted(df['stress_level'].unique())
    stress_filter = st.sidebar.multiselect("Nível de Estresse", options=stress_levels, default=stress_levels)
    
    df_filtered = df[df['stress_level'].isin(stress_filter)]

    st.subheader("📊 Correlação: Tempo de Celular vs. Performance")
    st.scatter_chart(data=df_filtered, x='daily_phone_hours', y='exam_score', color='stress_level')

    st.write("### 📋 Visualização de Dados (Amostra)")
    st.dataframe(df_filtered.head(10), use_container_width=True)

except Exception as e:
    st.error(f"⚠️ Erro ao carregar dados do banco SQLite: {e}")
    st.info("Verifique se o arquivo 'student_wellbeing.db' está na raiz do seu repositório GitHub.")