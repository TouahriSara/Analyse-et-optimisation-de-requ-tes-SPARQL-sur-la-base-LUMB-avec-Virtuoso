import requests
import json

# URL du fichier contenant les requêtes SPARQL
url = "https://swat.cse.lehigh.edu/projects/lubm/queries-sparql.txt"

# Télécharger le fichier SPARQL
response = requests.get(url)
if response.status_code == 200:
    queries_text = response.text
else:
    print("Erreur lors du téléchargement du fichier.")
    exit()

# Séparer les requêtes individuelles en fonction des doubles sauts de ligne
raw_queries = queries_text.split("\n\n")

# Préparer la liste des requêtes nettoyées sans commentaires
queries = []
for query in raw_queries:
    # Supprimer les lignes de commentaires et les lignes vides
    lines = query.splitlines()
    clean_lines = [line.strip() for line in lines if not line.strip().startswith("#") and line.strip()]
    # Reconstituer la requête sous forme de chaîne unique
    clean_query = " ".join(clean_lines).strip()
    # Ajouter la requête nettoyée si elle n'est pas vide
    if clean_query:
        queries.append(clean_query)

# Enregistrer les requêtes dans un fichier JSON
with open("queries.json", "w") as file:
    json.dump(queries, file, indent=4)

print("Les requêtes SPARQL ont été enregistrées sans commentaires dans queries.json.")
