import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('🚗 Análisis de anuncios de autos')

# Controles de visualización
hist_check = st.checkbox('📊 Mostrar histograma')
disp_check = st.checkbox('🔘 Mostrar gráfica de dispersión')
barr_check = st.checkbox('📈 Mostrar gráfica de barras por año')

# --- Histograma con slider para eje X (odómetro)
if hist_check:
    st.write('📊 Histograma: Distribución del odómetro en autos en venta')

    # Definir rango del odómetro para el slider
    min_odo = int(car_data['odometer'].min())
    max_odo = int(car_data['odometer'].max())

    odometer_range = st.slider(
        "Selecciona rango de odómetro para el histograma:",
        min_value=min_odo,
        max_value=max_odo,
        value=(min_odo, max_odo)
    )

    # Filtrar datos según rango seleccionado
    filtered_hist = car_data[
        car_data['odometer'].between(odometer_range[0], odometer_range[1])
    ]

    fig = px.histogram(filtered_hist, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de dispersión con sliders para ambos ejes
if disp_check:
    st.write('🔘 Gráfico de dispersión: Relación entre odómetro y precio')

    # Rango para odómetro
    min_odo = int(car_data['odometer'].min())
    max_odo = int(car_data['odometer'].max())

    # Rango para precio
    min_price = int(car_data['price'].min())
    max_price = int(car_data['price'].max())

    odometer_range = st.slider(
        "Selecciona rango de odómetro para dispersión:",
        min_value=min_odo,
        max_value=max_odo,
        value=(min_odo, max_odo)
    )

    price_range = st.slider(
        "Selecciona rango de precio para dispersión:",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price)
    )

    # Filtrar datos según rangos seleccionados
    filtered_disp = car_data[
        (car_data['odometer'].between(odometer_range[0], odometer_range[1])) &
        (car_data['price'].between(price_range[0], price_range[1]))
    ]

    fig = px.scatter(filtered_disp, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# --- Barras por rango de años
if barr_check:
    # Limpiar y ordenar los años
    ylist = car_data['model_year'].dropna().astype(int)
    min_year = int(ylist.min())
    max_year = int(ylist.max())

    # Slider para seleccionar el rango de años
    year_range = st.slider(
        "Selecciona un rango de años:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Filtrar por rango de años
    filtered_data = car_data[car_data['model_year'].between(year_range[0], year_range[1])]

    num_autos = filtered_data.shape[0]
    st.write(f'Total de autos en el rango seleccionado: {num_autos}')
    st.write(f'📈 Gráfico de barras: Precio de autos por año (de {year_range[0]} a {year_range[1]})')

    fig = px.bar(filtered_data, x='model_year', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)
