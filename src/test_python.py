print("hello")
import csv
import requests
import pandas
import folium

# lire le fichier csv et créer un DataFrame pandas
projet = pandas.read_csv('src/liste projet.csv')
print(projet.columns)

# création de la carte
map_mdm = folium.Map(location=(43.3062817,5.3795732),zoom_start=13)

# créer les icones à partir du DataFrame
lignes = len(projet)
for i in range(0,lignes):
    lieu = projet.iloc[i]['lieu']
    activite = projet.iloc[i]['activité']
    latitude = projet.iloc[i]['latitude']
    longitude = projet.iloc[i]['longitude']
    contact = projet.iloc[i]['contact']
    jour = projet.iloc[i]['jour']
    horaire = projet.iloc[i]['horaire']
    adresse = projet.iloc[i]['adresse']
    AME = projet.iloc[i]['AME']
    medecins  = projet.iloc[i]['consultation medecins']
    partenaires = projet.iloc[i]['consultation partenaires']
    orientation = projet.iloc[i]['orientation sociales']
    temoignages = projet.iloc[i]['lien et temoignages']
    rdr = projet.iloc[i]['rdr']
    telephone = projet.iloc[i]['telephone']
    social = projet.iloc[i]['social renforcé']


#    print('lieu, horaire ', lieu, horaire)

# Contenu HTML de la popup
    popup_html = f"""
    <b> {lieu}</b><br><br>
    <b>adresse :</b> {adresse}<br>
    <b>📞 Téléphone :</b> {telephone}<br>
    <b>✉️ email : </b><a href="mailto:{contact}">{contact}</a><br>
    <b>jour :</b> {jour}<br>
    <b>horaire :</b> {horaire}<br>
    """
    if  AME == "oui":
        popup_html +=  f"""<b> AME :</b> {AME}<br> """
    if  medecins == "oui":
        popup_html +=  f""" <b>consultation medecins :</b> {medecins}<br> """
    if partenaires == "oui":
        popup_html +=  f""" <b>consultation partenaires :</b> {partenaires}<br> """
    if orientation == "oui":
        popup_html +=  f""" <b>orientation sociales :</b> {orientation}<br> """
    if  temoignages == "oui":
        popup_html +=  f""" <b>lien et temoignages :</b> {temoignages}<br> """
    if rdr == "oui":
        popup_html +=  f""" <b>rdr :</b> {rdr}<br> """          
    if social == "oui":
        popup_html +=  f""" <b>social renforcé :</b> {social}<br> """      
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
