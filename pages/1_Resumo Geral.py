import streamlit as st
from utils.processamento import carrega_chegadas
import matplotlib.pyplot as plt
import seaborn as sns

df = carrega_chegadas()
sns.set_style("whitegrid")
@st.cache_data
st.title("Resumo Geral")

st.header('Top 10 Estados com mais Chegadas de Turistas em 2024')

total = df['chegadas'].sum()
uf_top = df.groupby('uf')['chegadas'].sum().sort_values(ascending=False).head(10)

fig1, ax1 = plt.subplots()
sns.barplot(
    x=uf_top.values,
    y=uf_top.index,
    palette="Blues_d",
    ax=ax1
)

for i, value in enumerate(uf_top.values):
    ax1.text(value + max(uf_top.values) * 0.01, i, f"{value:,}".replace(",", "."), va='center')

ax1.set_title('Estados com mais Chegadas de Turistas')
ax1.set_xlabel('Chegadas')
ax1.set_ylabel('Estado')
ax1.tick_params(axis='x', labelsize=0)
ax1.tick_params(axis='y', labelsize=12)

st.pyplot(fig1)

st.header('Chegadas por Continente')

continente_data = df.groupby('continente')['chegadas'].sum().sort_values(ascending=False).reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(
    data=continente_data,
    x='chegadas',
    y='continente',
    palette='Greens_d',
    ax=ax2
)

for i, value in enumerate(continente_data['chegadas']):
    ax2.text(value + max(continente_data['chegadas']) * 0.01, i, f"{value:,}".replace(",", "."), va='center')

ax2.set_title('Total de Chegadas por Continente em 2024', fontsize=14, weight='bold')
ax2.set_xlabel('Chegadas')
ax2.set_ylabel('Continente')

st.pyplot(fig2)
