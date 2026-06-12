import pandas as pd

# 1. Charger ton fichier Excel
df = pd.read_excel(r'C:\Users\alexandre.batisse\.vscode\Projet\Projet_Stage_Scalian\data\Raw\AdressesWOTIF.xlsx')  # Remplace par ton fichier
df.columns = ['latitude', 'longitude']  # Ajuste les noms de colonnes si nécessaire

# 2. Créer le contenu du fichier KML
kml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Points pour TIM-online</name>
    <description>2100 points à vérifier</description>
'''

# 3. Ajouter un point pour chaque ligne du DataFrame
for idx, row in df.iterrows():
    kml_content += f'''
    <Placemark>
      <name>Point {idx + 1}</name>
      <description>Lat: {row['latitude']}, Lon: {row['longitude']}</description>
      <Point>
        <coordinates>{row['longitude']},{row['latitude']}</coordinates>
      </Point>
    </Placemark>
'''

# 4. Fermer le fichier KML
kml_content += '''
  </Document>
</kml>
'''

# 5. Sauvegarder le fichier KML
with open(r'C:\Users\alexandre.batisse\.vscode\Projet\Projet_Stage_Scalian\data\Processed\points_pour_tim_online.kml', "w", encoding="utf-8") as f:
    f.write(kml_content)

print("✅ Fichier 'points_pour_tim_online.kml' généré avec succès !")
print("Tu peux maintenant l'importer dans TIM-online.")