import streamlit as st
from utils.processamento import carrega_chegadas

st.set_page_config(
  page_title='Descrição dos Dados',
  page_icon='🌎',
)

st.title('Descrição dos Dados')

st.header('Chegada de Turistas Internacionais - 2024')
st.markdown(
  """
    Estimativa das chegadas de turistas internacionais ao Brasil, por país, mês e via de acesso. Os dados vêm da Polícia Federal, seguem padrões da ONU Turismo e são tratados para excluir viajantes não turísticos, resultando em estatísticas comparáveis internacionalmente.
    
    **Linhas:** 22.857
    
    Disponível em: https://dados.gov.br/dados/conjuntos-dados/estimativas-de-chegadas-de-turistas-internacionais-ao-brasil
  """
)

st.header('Dataframe')
st.dataframe(carrega_chegadas())