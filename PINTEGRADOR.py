# -*- coding: utf-8 -*-
"""PI 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tBaEd40s8A6x7tzYH8scGfqUBcyEW8SM
"""

import pandas as pd
import plotly.express as px
import streamlit as st 



df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')


df = df.rename(columns={'totalCases': 'Número acumulado de casos','newCases': 'Novos casos','deaths': 'Número acumulado de óbitos','newDeaths': 'Novos óbitos','vaccinated': 'Vacinas aplicadas - primeira dose','vaccinated_second': 'Vacinas aplicadas - segunda dose','vaccinated_single': 'Vacinas aplicadas - dose única','tests': 'Testes Realizados'})


state  = 'SP'
estados = list(df['state'].unique())



colunas = ['Número acumulado de casos','Novos casos','Número acumulado de óbitos','Novos óbitos','Vacinas aplicadas - primeira dose','Vacinas aplicadas - segunda dose','Vacinas aplicadas - dose única','Testes Realizados',]
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)


df = df[df['state'] == state]

date_col = pd.DatetimeIndex(df['date'])

df['month'] = date_col.month + '/' + date_col.year

fig = px.line(df, x="month", y=column, title=column + ' - ' + state)
fig.update_layout( #xaxis_title='Data', yaxis_title=column.upper(),title = {'x':0.5}
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "line"],
                    label="Line",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
            direction="down",
        ),
    ]   
)

st.title('DADOS COVID-19')
st.write('Nessa aplicação, o usuário tem a possibilidade de interação,e visualização de dados sobre  covid-19. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Projeto desenvolvido por alunos UNIVESP,PROJETO INTEGRADOR IV')
