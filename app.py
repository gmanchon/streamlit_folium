
import streamlit as st

from streamlit_folium import folium_static

import folium


def color_zone(feat):

    # get zone code from json
    code = feat["properties"]["code"]

    # convert zone
    try:
        code = int(code)
    except ValueError:
        code = 0

    # convert zone code to color code
    return "#00{:02x}ff".format(int(code / 95 * 255))


# def highlight_zone(feat):
#     return "blue" if int(feat["properties"]["code"][:1]) < 5 else "green"


# center on France
m = folium.Map(location=[47, 1], zoom_start=6)

folium.GeoJson(
    "geojson.json",
    name="geojson",
    style_function=lambda feat: {
        "weight": 1,
        "color": "black",
        "opacity": 0.25,
        "fillColor": color_zone(feat),
        "fillOpacity": 0.25,
    },
    # highlight_function=lambda feat: {
    #     "fillColor": highlight_zone(feat),
    # },
).add_to(m)

# render map
folium_static(m)
