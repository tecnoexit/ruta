import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd
import geopandas as gpd
import base64
from folium import IFrame

def main():
    st.title("Mapa interactivo de Almirante Brown")
    
    # Cargar datos geoespaciales
    gpf = gpd.read_file("brown.json")
    gpf2 = gpd.read_file("lineas.json")
    # Crear un mapa con Folium
    m = folium.Map([-34.77709003427292, -58.3284992430521], zoom_start=15)
    tooltip = "Click para ver sensor"#es lo que aparece al pasar el cursor encima
    # Añadir los datos geoespaciales al mapa
    folium.GeoJson(gpf,style_function=lambda feature: {
        "fillColor": "green",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5"}).add_to(m)
    #añadir lineas al mapa 
    folium.GeoJson(gpf2,style_function=lambda feature: {
        "fillColor": "green",
        "color": "red",
        "weight": 10,
        "dashArray": "5, 5"}).add_to(m)
    # Mostrar el mapa en Streamlit
    #folium_static(m)
    #esta parte del codigo crea las variables y configuraciones para mostrar una foto al pulsar un popup
    html = '<img src="data:./images/1.png;base64,{}">'.format
    picture1 = base64.b64encode(open('./images/1.png','rb').read()).decode()
    iframe1 = IFrame(html(picture1), width=600+20, height=400+20)
    popup1 = folium.Popup(iframe1, max_width=650)
    icon1 = folium.Icon(color="red", icon="glyphicon-home")

     # Añadir los datos geoespaciales al map
    folium.Marker(location=[-34.77666669868428, -58.32769950365982],popup=popup1,tooltip=tooltip,icon=folium.Icon(color = 'red', icon='cloud')).add_to(m)
    folium.Marker(location=[-34.77651647270125, -58.3268370603236],popup='pablo',tooltip=tooltip,icon=folium.Icon(color='green', icon= "cloud")).add_to(m)
    folium.Marker(location=[-34.77724579128701, -58.33167765226253],popup='ferreteria',tooltip=tooltip,icon=folium.Icon(color='red', icon='envelope')).add_to(m)

    folium_static(m)

if __name__ == "__main__":
    main()
