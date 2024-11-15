import requests

# URL of the file containing SPARQL queries
url = "https://swat.cse.lehigh.edu/projects/lubm/queries-sparql.txt"

# Download the SPARQL file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    queries_text = response.text
else:
    print("Error fetching the file.")
    exit()

# Split the text into individual queries based on double newlines (empty lines between queries)
raw_queries = queries_text.split("\n\n")

# Prepare the list of cleaned queries
queries = []
for query in raw_queries:
    # Split each query into lines and remove comments or empty lines
    lines = query.splitlines()
    clean_lines = [line.strip() for line in lines if not line.strip().startswith("#") and line.strip()]
    
    # Join the cleaned lines back into a single query string
    clean_query = " ".join(clean_lines).strip()
    
    if clean_query:  # Add only non-empty queries
        queries.append(clean_query)

# Write the QUERIES array to a shell script file
with open("queries.sh", "w") as file:
    file.write("QUERIES=(\n")
    for query in queries:
        # Escape double quotes inside the query
        query = query.replace('"', '\\"')
        file.write(f'   "{query.strip()}"\n')
    file.write(")\n")

print("SPARQL queries successfully written to queries.sh")
