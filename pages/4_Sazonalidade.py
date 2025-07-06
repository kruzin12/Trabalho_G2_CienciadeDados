import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from utils.processamento import carrega_chegadas

df = carrega_chegadas()
st.title("Sazonalidade")

st.header('Evolução Mensal das Chegadas')
serie = df.groupby(['cod_mes', 'mes'])['chegadas'].sum().reset_index()
serie = serie.sort_values('cod_mes')

fig4, ax4 = plt.subplots()
sns.lineplot(data=serie, x='mes', y='chegadas', marker='o', ax=ax4)
ax4.set_title('Evolução Mensal das Chegadas')
ax4.set_xlabel('Mês')
ax4.set_ylabel('Chegadas')
plt.xticks(rotation=45)
st.pyplot(fig4)

st.header('Mapa de Calor Estado x Mês')
heatmap_data = (
    df.groupby(['uf', 'cod_mes'])['chegadas']
    .sum()
    .unstack(fill_value=0)
    .sort_index()
)

fig6, ax6 = plt.subplots(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='Blues', ax=ax6)
ax6.set_title('Chegadas por Estado e Mês')
ax6.set_xlabel('Mês')
ax6.set_ylabel('Estado')
st.pyplot(fig6)