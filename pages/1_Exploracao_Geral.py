import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações gerais
st.set_page_config(page_title="Exploração Geral dos Dados", layout="wide")
sns.set(style="whitegrid")

# Carregamento dos dados
df = pd.read_csv("dados/housing.csv")

st.title("📊 Exploração Geral dos Dados de Moradia na Califórnia")

st.markdown("""
Nesta seção, apresentamos gráficos estáticos que mostram como estão distribuídas a **renda mediana**, o **valor das casas** e a **população média** das regiões da Califórnia,
de acordo com a proximidade ao oceano. As visualizações são baseadas em todo o conjunto de dados, sem filtros aplicados.
""")

# Gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Distribuição da Renda Mediana")
    st.markdown("Este histograma mostra quantas regiões apresentam determinada faixa de **renda mediana** (em múltiplos de US$ 10 mil).")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df["median_income"], bins=30, kde=False, color="#1f77b4", ax=ax)
    ax.set_xlabel("Renda Mediana ($10 mil)")
    ax.set_ylabel("Número de Regiões")
    st.pyplot(fig)

with col2:
    st.subheader("🏠 Distribuição do Valor das Casas")
    st.markdown("Este gráfico mostra como os **valores medianos das casas** estão distribuídos entre as regiões.")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df["median_house_value"], bins=30, kde=False, color="#ff7f0e", ax=ax)
    ax.set_xlabel("Valor Mediano das Casas (US$)")
    ax.set_ylabel("Número de Regiões")
    st.pyplot(fig)

st.subheader("👥 Distribuição da População por Proximidade ao Oceano")
st.markdown("Boxplot mostrando a variação da população entre regiões com diferentes proximidades ao oceano.")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x="ocean_proximity", y="population", data=df, ax=ax, palette="Set2")
ax.set_xlabel("Proximidade ao Oceano")
ax.set_ylabel("População")
st.pyplot(fig)

