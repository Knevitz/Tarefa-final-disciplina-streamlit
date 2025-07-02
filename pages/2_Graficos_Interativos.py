import streamlit as st
import pandas as pd
import plotly.express as px

# Dados
df = pd.read_csv("dados/housing.csv")
df["median_income_dollars"] = df["median_income"] * 10000

st.title("📈 Gráficos Interativos")

# Filtros
st.sidebar.header("Filtros Interativos")
renda_em_dolares = st.sidebar.slider(
    "Renda Mediana Mínima (US$)", 
    int(df["median_income_dollars"].min()), 
    int(df["median_income_dollars"].max()), 
    20000,
    step=1000,
    format="$%d"
)

# Filtrar
df_filtrado = df[df["median_income_dollars"] >= renda_em_dolares]

st.subheader("🏠 Valor das Casas em Relação à Renda Mediana")
st.markdown(
    "Cada ponto representa uma região; a cor indica a proximidade ao oceano, "
    "o tamanho representa a população e ao passar o mouse aparecem mais informações."
)

fig1 = px.scatter(
    df_filtrado,
    x="median_income_dollars",
    y="median_house_value",
    color="ocean_proximity",
    size="population",
    hover_data=["total_rooms", "population"],
    color_discrete_sequence=px.colors.qualitative.Plotly,  # cores mais fortes aqui
    labels={
        "median_income_dollars": "Renda Mediana (US$)",
        "median_house_value": "Valor Mediano das Casas (US$)",
        "ocean_proximity": "Proximidade ao Oceano",
        "population": "População",
        "total_rooms": "Total de Quartos"
    },
)

fig1.update_layout(
    xaxis=dict(tickprefix="$", gridcolor="LightGray"),
    yaxis=dict(tickprefix="$", gridcolor="LightGray"),
    plot_bgcolor="white",
    legend_title_text="Proximidade ao Oceano",
    margin=dict(l=40, r=40, t=50, b=40)
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("🌊 População Média por Proximidade ao Oceano")
st.markdown(
    "Gráfico de barras interativo mostrando a média da população por categoria de proximidade ao oceano."
)
df_media = df_filtrado.groupby("ocean_proximity", as_index=False)["population"].mean()

fig2 = px.bar(
    df_media,
    x="population",
    y="ocean_proximity",
    orientation="h",
    color="ocean_proximity",
    color_discrete_sequence=px.colors.qualitative.Set2,
    labels={"population": "População Média", "ocean_proximity": "Proximidade ao Oceano"},
    title="População Média por Proximidade ao Oceano",
)

fig2.update_layout(
    xaxis=dict(tickformat=",", gridcolor="LightGray"),
    plot_bgcolor="white",
    showlegend=False,
    margin=dict(l=40, r=40, t=50, b=40),
)
st.plotly_chart(fig2, use_container_width=True)
