# 📊 Student Productivity & Wellbeing Data Pipeline

Este projeto implementa um pipeline de dados **End-to-End** que integra
informações de comportamento digital (tempo de tela), performance
acadêmica e dados climáticos em tempo real.

O objetivo é demonstrar habilidades práticas em **engenharia de dados**,
incluindo ingestão de múltiplas fontes, transformação, modelagem
analítica e visualização em dashboard.

------------------------------------------------------------------------

# 🧠 Problema Proposto

O projeto busca responder uma pergunta simples:

**Existe relação entre uso de smartphone, fatores ambientais e
desempenho acadêmico?**

Para explorar isso, o pipeline integra três tipos de dados:

-   📱 Uso de smartphone (tempo de tela)
-   🎓 Performance acadêmica
-   🌤️ Condições climáticas externas

Essas informações são processadas e consolidadas em um **dataset
analítico final**, permitindo análises de correlação e visualização
interativa.

------------------------------------------------------------------------

# 🏗️ Arquitetura do Projeto

O pipeline segue os princípios da **Medallion Architecture**, separando
o processamento em camadas de qualidade de dados.

## Bronze --- Raw Layer

Responsável pela ingestão de dados brutos.

-   Arquivos CSV locais
-   API externa de clima (WeatherAPI)

------------------------------------------------------------------------

## Silver --- Cleaned Layer

Tratamento e padronização:

-   snake_case nas colunas
-   limpeza de chaves primárias
-   conversão de tipos
-   tratamento de valores nulos

Ferramenta principal: **Pandas**

------------------------------------------------------------------------

## Gold --- Curated Layer

-   Join entre datasets
-   Enriquecimento com dados climáticos
-   Persistência no banco

Banco utilizado: **PostgreSQL**

------------------------------------------------------------------------

# 🛠️ Tecnologias

-   Python
-   Pandas
-   NumPy
-   SQLAlchemy
-   PostgreSQL
-   Docker
-   Streamlit

------------------------------------------------------------------------

# 📂 Estrutura

    app/
    dataset/
    scripts/
    sql/
    docker-compose.yml
    main.py
    requirements.txt
    .env

------------------------------------------------------------------------

# ⚙️ Execução

## Clonar

    git clone https://github.com/seu-usuario/data-pipeline-student.git
    cd data-pipeline-student

## Ambiente

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Infra

    docker-compose up -d

## Pipeline

    python main.py

## Dashboard

    streamlit run app/dashboard.py

------------------------------------------------------------------------

# 📈 Insights

-   Relação entre tempo de tela e notas
-   Padrões de comportamento digital
-   Influência de clima na produtividade

------------------------------------------------------------------------

# 🎯 Objetivo

Demonstrar habilidades em:

-   Engenharia de Dados
-   ETL
-   APIs
-   Docker
-   PostgreSQL
-   Streamlit

------------------------------------------------------------------------

# 👨‍💻 Autor

Projeto desenvolvido para portfólio em **Data Engineering e Python**.
