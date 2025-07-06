import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from utils.processamento import carrega_chegadas

df = carrega_chegadas()
st.title("Chegadas por UF no Brasil")

import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from utils.processamento import carrega_chegadas

st.set_page_config(page_title="Mapa Coroplético - Chegadas", layout="wide")

#Carrega os dados tratados
df = carrega_chegadas()

#Junta chegadas e estado
df_uf = df.groupby('uf')['chegadas'].sum().reset_index()

#Carrega o GeoJSON com siglas dos estados
geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
geojson = requests.get(geojson_url).json()

#Mapa
fig = px.choropleth(
    df_uf,
    geojson=geojson,
    locations='uf',
    featureidkey='properties.name',
    color='chegadas',
    color_continuous_scale='Viridis',
    title='Chegadas de Turistas por Estado (2024)',
    hover_name='uf',
    labels={'chegadas': 'Chegadas'}
)

fig.update_traces(marker_line_width=0.5, marker_line_color='black')
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)


st.title('Análise Interativa por Estado e Mês')

estado = st.selectbox("Selecione a UF", sorted(df['uf'].unique()))

#Cria dicionário auxiliar para nome dos meses
MESES = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

#Gera lista de meses únicos ordenada por cod mes
meses_ordenados = (
    df[['cod_mes', 'mes']]
    .drop_duplicates()
    .sort_values('cod_mes')
    ['mes']
    .tolist()
)

#Cria selectbox com ordem correta
mes = st.selectbox("Selecione o mês", meses_ordenados)

filtro = df[(df['uf'] == estado) & (df['mes'] == mes) & (df['chegadas'] >= 10)]

fig = px.bar(
    filtro,
    x='pais',
    y='chegadas',
    color='via',
    title='Chegadas por País e Via',
    labels={
        'chegadas': 'Chegadas',
        'pais': 'País',
        'via': 'Via'
    }
)
st.plotly_chart(fig)
