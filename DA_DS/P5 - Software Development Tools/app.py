import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('files/datasets/input/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button=st.button('Construir gráfico de dispersión')        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 


if scatter_button:
    
    st.write('Creacion de un diagrama de dispersión')

    fig=px.scatter(car_data)

    st.plotly_chart(fig,use_container_width=True)

