import webbrowser
import time

# 1. Charge les liens depuis ton fichier texte
with open(r"C:\Users\alexandre.batisse\.vscode\Projet\Projet_Stage_Scalian\data\Raw\Adresses WO TIF.txt", "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

print(f"✅ {len(links)} liens chargés depuis 'Adresses WO TIF.txt'")

# 2. Ouvre chaque lien dans le navigateur (un par un)
for i, link in enumerate(links, 1):
    print(f"\n[{i}/{len(links)}] Ouverture du lien : {link[:60]}...")
    webbrowser.open(link)  # Ouvre dans le navigateur par défaut
    time.sleep(5)  # Attend 5 secondes pour laisser le temps au navigateur de charger la page

print("\n✨ Tous les liens ont été ouverts dans ton navigateur !")
print("Les téléchargements devraient démarrer automatiquement.")