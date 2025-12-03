print("hello")
import csv
import requests
import pandas
import folium

# lire le fichier csv et créer un DataFrame pandas
projet = pandas.read_csv('src/liste projet.csv')
# print(projet)

# création de la carte
map_mdm = folium.Map(location=(43.2898668,5.3834864),zoom_start=5)

# créer les icones à partir du DataFrame
lignes = len(projet)
for i in range(0,lignes):
    lieu = projet.iloc[i]['lieu']
    aide = projet.iloc[i]['aide']
    activite = projet.iloc[i]['activité']
    latitude = projet.iloc[i]['latitude']
    longitude = projet.iloc[i]['longitude']
    contact = projet.iloc[i]['contact']
    frequence = projet.iloc[i]['fréquence']
    horaire = projet.iloc[i]['horaire']

#    print('lieu, horaire ', lieu, horaire)

# Contenu HTML de la popup
    popup_html = f"""
    <b>Information :</b><br><br>
    lieu : {lieu}<br>
    ✉️ Email : <a href="mailto:{contact}">{contact}</a><br>
    horaire : {horaire}<br>
    """
#    print('popup : ', popup_html)

# Ajout du marqueur
    folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=lieu
    ).add_to(map_mdm)

# Sauvegarder la carte dans un fichier HTML
map_mdm.save("carte_projets_mdm.html")

print("Carte créée : ouvrez 'carte_projets_mdm' dans votre navigateur.")
