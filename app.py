import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Creación de gráficos en función del kilometraje de un vehiculo')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
build_histogram=st.checkbox('Construir un histograma') # Crear un botón

if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma sobre el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig=px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# construir un grafico de dispersión
build_scatter=st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión en base al precio y kilometraje')

    # crear un grafico de dispersion
    fig=px.scatter(car_data, y="price", x="odometer")

    # mostrar un grafico plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_pie_chart = st.checkbox("Construir un gráfico de pastel")

if build_pie_chart:
    # escribir un mensaje
    st.write('Creación de un gráfico de pastel en base a la cantidad de autos vendidos por modelo')

    # Agrupar los datos por "model" y contar la cantidad de autos por modelo
    model_counts = car_data["model"].value_counts().reset_index()
    model_counts.columns = ["model", "count"]  # Renombrar las columnas para usarlas en el gráfico

    # Crear un gráfico de pastel con Plotly
    fig = px.pie(model_counts, values="count", names="model", title="Cantidad de autos por modelo")

    # Mostrar un gráfico de pastel interactivo
    st.plotly_chart(fig, use_container_width=True)
