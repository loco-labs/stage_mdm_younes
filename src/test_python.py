print("hello")
import csv
with open('src/liste.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
import folium
l=folium.Map(location=(43.2898668,5.3834864),zoom_start=5)
folium.Marker(
    location=[48.8588255,2.2646331],
    tooltip="Click me!",
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(l)

folium.Marker(
    location=[43.292614, 5.366633],
    tooltip="Click me!",
    popup="Timberline Lodge",
    icon=folium.Icon(color="green"),
).add_to(l)
m = folium.Map(location=[-71.38, -73.9], zoom_start=11)

trail_coordinates = [
    (43.2802207,5.2158271),
    (43.6006738,1.3504412),
    (44.8636882,-0.6684134),
    (47.2382037,-1.6427356),
    (48.8588255,2.2646331),
]
folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(l)
l.save("montre.html")