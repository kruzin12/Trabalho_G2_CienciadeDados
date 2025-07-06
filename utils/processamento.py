import pandas as pd
import streamlit as st
import json

@st.cache_data
def carrega_chegadas():
    df = pd.read_csv('./trabalho_G2/data/chegadas_2024.csv', encoding='latin-1', sep=';')
    df.columns = df.columns.str.strip()
    #Remover codigo da via
    df = df.drop(columns=['cod via'])
    
    NOMES_COLUNAS = {
        'Continente':'continente',
        'cod continente':'cod_continente',
        'País':'pais',
        'cod pais':'cod_pais',
        'UF':'uf',
        'cod uf':'cod_uf',
        'Via':'via',
        'Mês':'mes',
        'cod mes':'cod_mes',
        'Chegadas': 'chegadas'
    }
    
    #Renomeia as colunas
    df.columns = df.columns.str.strip()
    df = df.rename(columns=NOMES_COLUNAS)

    #Remove UF invalido
    df = df[df['cod_uf'] != 99]
    df = df.dropna()

    #Remove linhas descartaveis
    df = df.drop_duplicates()
    df = df.drop(df[df['pais'] == 'Países não especificados'].index)
    df = df.drop(df[df['continente'] == 'Continente não especificado'].index)

    #Converte valores numericos
    df['chegadas'] = pd.to_numeric(df['chegadas'], errors='coerce').fillna(0)

    return df
