import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.processamento import carrega_chegadas

df = carrega_chegadas()
st.title("Análise por UF")

st.header('Chegadas por País e Via de Entrada')

# Filtro por estado
estado = st.selectbox("Selecione o Estado", sorted(df['uf'].unique()))
df_estado = df[df['uf'] == estado]

# Gráfico de países x via
fig1, ax1 = plt.subplots(figsize=(10, 6))
df_pais_via = df_estado.groupby(['pais', 'via'])['chegadas'].sum().reset_index()
df_pivot = df_pais_via.pivot(index='pais', columns='via', values='chegadas').fillna(0)
df_pivot = df_pivot[df_pivot.sum(axis=1) > 0].sort_values(by=df_pivot.columns.tolist(), ascending=False).head(10)
df_pivot.plot(kind='barh', stacked=True, ax=ax1, colormap='tab20')
ax1.set_title(f'Principais Países de Origem por Via - {estado}')
ax1.set_xlabel('Chegadas')
ax1.set_ylabel('País')
st.pyplot(fig1)

# Gráfico de chegadas por via de transporte
st.header('Chegadas por Via de Transporte')
fig2, ax3 = plt.subplots()
via_data = df.groupby('via')['chegadas'].sum().reset_index()
sns.barplot(data=via_data, x='chegadas', y='via', ax=ax3, palette='Set2')
ax3.set_title('Chegadas por Via de Transporte')
ax3.set_xlabel('Chegadas')
ax3.set_ylabel('Via')
st.pyplot(fig2)