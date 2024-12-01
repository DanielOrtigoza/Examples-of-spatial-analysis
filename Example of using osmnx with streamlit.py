


import streamlit as st
import osmnx as ox
import folium
import os

class interactive_map:
  def __init__(self) -> None:
    pass


  def show_map(self):
    st.title("Street explorer")
    lat = st.number_input("Latitude", value = 40.748817)  # Ejemplo: NY
    lon = st.number_input("Longitude", value = -73.985428)
    distance = st.slider("Distance to search (in meters)", min_value = 100, max_value = 5000, value = 1000)

    if st.button("Search for streets"):

      final_map = folium.Map(location = [lat, lon], zoom_start = 14)

      graph = ox.graph_from_point((lat, lon), dist = distance, network_type = "drive")
      nodes = graph.nodes(data = True)

      for node, data in nodes:
        folium.Marker(
          location = [data['y'], data['x']],
        ).add_to(final_map)

      # Guardar el mapa como un archivo HTML
      map_path = "mapa_interactivo.html"
      final_map.save(map_path)

      # Mostrar el archivo HTML en Streamlit
      with open(map_path, "r") as f:
          map_html = f.read()
      st.components.v1.html(map_html, height=600, width=700)


final = interactive_map()
final.show_map()


