import pandas as pd
import plotly_express as px
import streamlit as st

st.header('Dados de Anúncios de Vendas de Carros')
st.write('Clique em um dos botões para visualizar os dados.')
car_data = pd.read_csv("assets/vehicles.csv", sep=',') # lendo os dados
hist_button = st.button('Criar Histograma') # criar um botão para mostrar o Histograma
disp_button = st.button('Criar Dispersão') # criar um botão para mostrar a Dispersão

if hist_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)

if disp_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando uma dispersão para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um gráfico de dispersão
            fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)