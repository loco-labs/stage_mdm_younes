print("hello")
import csv
import requests
import pandas
import folium
import folium

# Coordonnées de l'endroit où placer le marqueur
latitude = 43.28498595454043 
longitude = 5.393399663866488

# Informations à afficher
telephone = "+33 4 86 11 09 26"
email = "contact@example.com"
jours_ouverts = """

Lundi : 13;30h - 15;30h<br>,
Mardi : Fermé,
Mercredi : 9h - 11h<br>,
Jeudi : Fermé,
Vendredi : 9h - 11h<br>,
Samedi : Fermé,
Dimanche : Fermé
"""
# Contenu HTML de la popup
popup_html = f"""
<b>Contact :</b><br>
📞 Téléphone : {telephone}<br>
✉️ Email : <a href="mailto:{email}">{email}</a><br><br>
<b>Jours d'ouverture :</b><br>
{jours_ouverts}
"""


# Création de la carte centrée sur le monde
carte = folium.Map(location=[46.5, 2.5], zoom_start=5)

# Ajout du marqueur
folium.Marker(
    location=[43.28498595454043, 5.393399663866488],
    popup=folium.Popup(popup_html, max_width=300),
    tooltip="Médecins du Monde"
).add_to(carte)

# Sauvegarder la carte dans un fichier HTML
carte.save("carte_interactive.html")

print("Carte créée : ouvrez 'carte_interactive.html' dans votre navigateur.")