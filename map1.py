# map1.py

import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEVATION"])
vol = list(data["VOLCANOES"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[22.546127502350828,
            78.99302799585564], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, vl in zip(lat, lon, elev, vol):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=vl+": "+str(el)+" feet",
    fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("index.html")
