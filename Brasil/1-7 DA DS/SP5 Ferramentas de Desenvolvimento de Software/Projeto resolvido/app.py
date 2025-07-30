import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Ler os dados
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho
st.header('🚗 Análise de anúncios de carros')

# Controles de visualização
hist_check = st.checkbox('📊 Mostrar histograma')
disp_check = st.checkbox('🔘 Mostrar gráfico de dispersão')
barr_check = st.checkbox('📈 Mostrar gráfico de barras por ano')

# Histograma com controle deslizante para o eixo X (odômetro)
if hist_check:
    st.write('📊 Histograma: Distribuição do odômetro nos carros à venda')

    # Definir faixa do odômetro para o controle deslizante
    min_odo = int(car_data['odometer'].min())
    max_odo = int(car_data['odometer'].max())

    odometer_range = st.slider(
        "Selecione a faixa do odômetro para o histograma:",
        min_value=min_odo,
        max_value=max_odo,
        value=(min_odo, max_odo)
    )

    # Filtrar dados de acordo com a faixa selecionada
    filtered_hist = car_data[
        car_data['odometer'].between(odometer_range[0], odometer_range[1])
    ]

    fig = px.histogram(filtered_hist, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão com controles deslizantes para ambos os eixos
if disp_check:
    st.write('🔘 Gráfico de dispersão: Relação entre odômetro e preço')

    # Faixa para odômetro
    min_odo = int(car_data['odometer'].min())
    max_odo = int(car_data['odometer'].max())

    # Faixa para preço
    min_price = int(car_data['price'].min())
    max_price = int(car_data['price'].max())

    odometer_range = st.slider(
        "Selecione a faixa do odômetro para o gráfico de dispersão:",
        min_value=min_odo,
        max_value=max_odo,
        value=(min_odo, max_odo)
    )

    price_range = st.slider(
        "Selecione a faixa de preço para o gráfico de dispersão:",
        min_value=min_price,
        max_value=max_price,
        value=(min_price, max_price)
    )

    # Filtrar dados de acordo com as faixas selecionadas
    filtered_disp = car_data[
        (car_data['odometer'].between(odometer_range[0], odometer_range[1])) &
        (car_data['price'].between(price_range[0], price_range[1]))
    ]

    fig = px.scatter(filtered_disp, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de barras por faixa de anos
if barr_check:
    # Limpar e ordenar os anos
    ylist = car_data['model_year'].dropna().astype(int)
    min_year = int(ylist.min())
    max_year = int(ylist.max())

    # Controle deslizante para selecionar a faixa de anos
    year_range = st.slider(
        "Selecione uma faixa de anos:",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Filtrar pela faixa de anos
    filtered_data = car_data[car_data['model_year'].between(year_range[0], year_range[1])]

    num_autos = filtered_data.shape[0]
    st.write(f'Total de carros na faixa selecionada: {num_autos}')
    st.write(f'📈 Gráfico de barras: Preço dos carros por ano (de {year_range[0]} a {year_range[1]})')

    fig = px.bar(filtered_data, x='model_year', y='price', color='type')
    st.plotly_chart(fig, use_container_width=True)