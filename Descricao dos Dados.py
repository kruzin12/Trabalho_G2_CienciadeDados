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
st.markdown(
    """
    ---
    ## Como Navegar entre as Seções

    O dashboard é dividido em **quatro páginas**:

    - **Resumo Geral**: Apresenta os principais estados em número de chegadas.
    - **Mapas Interativos**: Permite explorar os dados por UF e mês com filtros dinâmicos, também mostra um mapa interativo por UF.
    - **Análise UF**: Foca nas características de cada estado individualmente.
    - **Sazonalidade**: Analisa a variação mensal e a quantidade de chegadas por mês com o mapa de calor.

    ---

    ## Como os Filtros Influenciam os Dados

    As páginas interativas incluem **filtros de UF (estado)** e **mês**, que:

    - **Atualizam os gráficos automaticamente**, refletindo apenas os dados daquele estado ou mês escolhido.
    - Permitem comparações específicas e análises mais precisas por região e período.
    - Alguns gráficos também se adaptam ao tipo de **via de entrada (aérea, marítima, terrestre, etc.)**.

    Utilize os filtros para ajustar a visualização conforme o seu interesse e obter insights personalizados.
    """
)
