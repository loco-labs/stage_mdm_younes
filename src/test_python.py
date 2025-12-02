print("hello")
import csv
import requests
import pandas
import folium
import folium

# Coordonnées de l'endroit où placer le marqueur
latitude = 43.2850044
longitude = 5.3908346

# Informations à afficher
telephone = "+33 4 86 11 09 26"
email = "contact@example.com"

# Contenu HTML du popup
popup_html = f"""
<b>Contact :</b><br>
📞 Téléphone : {telephone}<br>
✉️ Email : <a href="mailto:{email}">{email}</a>
"""

# Création de la carte centrée sur le monde
carte = folium.Map(location=[20, 0], zoom_start=2)

# Ajout du marqueur
folium.Marker(
    location=[latitude, longitude],
    popup=folium.Popup(popup_html, max_width=300),
    tooltip="Médecins du Monde"
).add_to(carte)

# Sauvegarder la carte dans un fichier HTML
carte.save("carte_interactive.html")

print("Carte créée : ouvrez 'carte_interactive.html' dans votre navigateur.")