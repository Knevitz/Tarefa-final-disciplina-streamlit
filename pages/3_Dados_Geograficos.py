import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Dados
df = pd.read_csv("dados/housing.csv")

st.title("🗺️ Mapa Geográfico das Moradias na Califórnia")

st.markdown("""
Visualização interativa da localização das moradias com base em latitude e longitude. 
A cor representa o valor da casa, e o tamanho o total da população.
""")

# Filtros
st.sidebar.header("Filtros Geográficos")

valor_max = st.sidebar.slider(
    "Valor máximo das casas (US$)", 
    float(df["median_house_value"].min()), 
    float(df["median_house_value"].max()), 
    float(df["median_house_value"].max())
)
df = df[df["median_house_value"] <= valor_max]

renda_min = st.sidebar.slider(
    "Renda mediana mínima (em múltiplos de US$10.000)", 
    float(df["median_income"].min()), 
    float(df["median_income"].max()), 
    2.0
)
df = df[df["median_income"] >= renda_min]

st.subheader("Localização das Casas na Califórnia")
fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    color="median_house_value",
    size="population",
    hover_name="ocean_proximity",
    hover_data={"median_income": True, "median_house_value": True},
    color_continuous_scale="viridis",
    size_max=15,
    zoom=5,
    height=650
)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig, use_container_width=True)
