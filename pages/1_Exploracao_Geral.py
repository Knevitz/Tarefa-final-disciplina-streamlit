import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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

# Gráfico boxplot
st.subheader("🌊 Distribuição da População por Proximidade ao Oceano")
st.markdown("Boxplot mostrando a variação da população entre regiões com diferentes proximidades ao oceano.")

fig, ax = plt.subplots(figsize=(10, 15))
sns.boxplot(
    x="ocean_proximity",
    y="population",
    data=df,
    ax=ax,
    hue="ocean_proximity",
    palette="Set2",
    legend=False,
    dodge=False,
    width=0.8,
    showfliers=True
)

ax.set_xlabel("Proximidade ao Oceano")
ax.set_ylabel("População")
ax.tick_params(axis='x', rotation=30)
ax.set_ylim(0, 30000)


ticks_100 = np.arange(0, 5100, 500)
ticks_5000 = np.arange(10000, 30001, 5000)
custom_ticks = np.concatenate([ticks_100, ticks_5000])
ax.set_yticks(custom_ticks)

fig.tight_layout()
st.pyplot(fig)
