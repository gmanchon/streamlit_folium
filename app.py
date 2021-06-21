
import streamlit as st

from streamlit_folium import folium_static

import folium


def color_department(feat):

    # get dpt code
    code = feat["properties"]["code"]

    # convert dpt
    try:
        code = int(code)
    except ValueError:
        code = 0

    # convert dpt to hex
    return "#0000{:02x}".format(int(code / 95 * 255))


def highlight_department(feat):
    return "blue" if int(feat["properties"]["code"][:1]) < 5 else "green"


# center on France
m = folium.Map(location=[47, 1], zoom_start=6)

folium.GeoJson(
    "geojson.json",
    name="geojson",
    style_function=lambda feat: {
        "weight": 1,
        "color": "black",
        "fillColor": color_department(feat),
        "opacity": 0.25,
        "fillOpacity": .25,
    },
    highlight_function=lambda feat: {
        "fillColor": highlight_department(feat),
    }
).add_to(m)

# render map
folium_static(m)
