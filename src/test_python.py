print("hello")
import csv
import requests
import pandas
import folium

with open('src/liste.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    for row in spamreader:
        print(', '.join(row))

amis = pandas.read_csv('src/liste.csv')
print(amis)
print(amis.iloc[2])
print(amis.iloc[2]['prenom'])

for i in range(0,3):
    print('prenom', amis.iloc[i]['prenom'])
print(amis['nom'])
#_______________________________________________________________________________________

l=folium.Map(location=(43.2898668,5.3834864),zoom_start=5)
folium.Marker(
    location=[48.8588255,2.2646331],
    tooltip="Paris!",
    popup="paname",
    icon=folium.Icon(icon="cloud"),
).add_to(l)

folium.Marker(
    location=[43.292614, 5.366633],
    tooltip="Marseille",
    popup="la ville bleue",
    icon=folium.Icon(color="noir"),
).add_to(l)
#___________________________________________________________

trail_coordinates = [
    (43.2802207,5.2158271),
    (43.6006738,1.3504412),
    (44.8636882,-0.6684134),
    (47.2382037,-1.6427356),
    (48.8588255,2.2646331),
]

# __________________________________________________________________

folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(l)

ls = folium.PolyLine(
    locations=[[36.75, 3.06], [36.75, 5.07], [35.39, 5.37], [35.3507, 3.3641], [36.75, 3.06]], color="red"
)

ls.add_child(folium.Popup("outline Popup on Polyline"))
ls.add_to(l)

gj = folium.GeoJson(
    data={"type": "Polygon", "coordinates": [[[27, 43], [33, 43], [33, 47], [27, 47]]]}
)

gj.add_child(folium.Popup("outline Popup on GeoJSON"))
gj.add_to(l)
#_______________________________________________________________________


state_geo = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()
state_data = pandas.read_csv(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_unemployment_oct_2012.csv"
)


folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(l)

folium.LayerControl().add_to(l)
l.save("montre.html")