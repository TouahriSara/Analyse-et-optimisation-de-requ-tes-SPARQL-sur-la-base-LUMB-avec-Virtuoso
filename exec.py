import json
import subprocess
import time

# Chemin vers le fichier JSON contenant les requêtes SPARQL
queries_file_path = r"C:\Users\pc\Desktop\TouahriSara\pfe\Touahrisaha_Analyse_RDF_LUMB\queries.json"

# URL de l'endpoint SPARQL de Virtuoso (à ajuster selon le conteneur)
sparql_endpoint = "http://localhost:8890/sparql"

# Fichier CSV de sortie pour stocker les résultats et les temps d'exécution
output_csv_path = "query_results_execution_times.csv"

# Charger les requêtes depuis le fichier JSON
with open(queries_file_path, "r") as file:
    queries = json.load(file)

# Nombre d'exécutions pour chaque requête pour obtenir la moyenne
num_runs = 5

# Ouvrir le fichier CSV pour écrire les résultats
with open(output_csv_path, mode="w") as file:
    file.write("query,execution_time_ms\n")  # Écrire l'en-tête

    # Exécuter chaque requête et enregistrer les résultats
    for query in queries:
        times = []  # Liste pour stocker les temps d'exécution de chaque exécution de la requête

        for _ in range(num_runs):
            # Mesurer le temps d'exécution en millisecondes
            start_time = time.time() * 1000  # Multiplie par 1000 pour obtenir des millisecondes

            try:
                # Exécuter la requête SPARQL avec curl
                result = subprocess.check_output([
                    "curl", "-s", "-X", "POST",
                    "--data-urlencode", f"query={query}",
                    sparql_endpoint
                ])
                result = result.decode("utf-8")  # Décoder le résultat en UTF-8
                success = True
            except subprocess.CalledProcessError as e:
                result = f"Erreur lors de l'exécution de la requête: {e}"
                success = False

            # Calculer le temps d'exécution
            execution_time_ms = int(time.time() * 1000 - start_time)
            times.append(execution_time_ms)

        # Calculer la moyenne des temps d'exécution
        avg_execution_time = sum(times) / num_runs
        file.write(f"\"{query}\",{avg_execution_time}\n")

print(f"Les résultats et les temps d'exécution ont été enregistrés dans {output_csv_path}.")
