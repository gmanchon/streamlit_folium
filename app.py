
import streamlit as st

from streamlit_folium import folium_static

import folium


def color_department(feat):
    return "lightblue" if int(feat["properties"]["code"][:1]) < 5 else "red"


def highlight_department(feat):
    return "blue" if int(feat["properties"]["code"][:1]) < 5 else "green"


# center on France
m = folium.Map(location=[47, 1], zoom_start=6)

folium.GeoJson(
    "geojson.json",
    name="geojson",
    style_function=lambda feat: {
        "weight": 2,
        "color": "black",
        "fillColor": color_department(feat),
    },
    highlight_function=lambda feat: {
        "fillColor": highlight_department(feat),
    }
).add_to(m)

# render map
folium_static(m)
