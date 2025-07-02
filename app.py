import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Habitação na Califórnia", layout="wide")

st.title("🏠 Dashboard de Habitação na Califórnia")

# Carregar dados
df = pd.read_csv("dados/housing.csv")

# Estatísticas
total_registros = len(df)
idade_media = round(df["housing_median_age"].mean(), 1)
preco_medio = round(df["median_house_value"].mean(), 2)

# Cards informativos
col1, col2, col3 = st.columns(3)
col1.metric("📌 Total de Registros", f"{total_registros:,}".replace(",", "."))
col2.metric("📅 Idade Média das Casas", f"{idade_media} anos")
col3.metric("💰 Preço Médio das Casas", f"US$ {preco_medio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

st.markdown("""
---

### 🔀 Como navegar:
- Utilize o menu lateral para acessar as diferentes seções do dashboard.
- Aplique os filtros disponíveis para refinar as visualizações.

### 🎯 Objetivo:
Explorar padrões e relações entre localização, renda, população e valor das moradias.
""")
