import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto 5')

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Al hacer clic en el botón de histograma
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Al hacer clic en el botón de gráfico de dispersión
if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="price", y="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)