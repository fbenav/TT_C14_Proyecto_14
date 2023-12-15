import pandas as pd
import plotly.express as px
import streamlit as st


st.header("Dashboard Proyecto 4 del bootcamp")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.checkbox('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
disper_button = st.button('Construir un gráfico de disperción') # crear un botón

if disper_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de disperción para el conjunto de datos de anuncios de venta de coches')
    
    # crear un grafico de disperción
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)