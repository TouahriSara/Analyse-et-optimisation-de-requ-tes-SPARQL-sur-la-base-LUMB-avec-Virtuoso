#!/bin/bash

# File to store the output
output_file="query_execution_times.csv"

# Write the header to the CSV file
echo "query,execution_time" > $output_file


# Source the SPARQL queries from queries.sh
source ./queries.sh


# Iterate over each query and execute it on the Virtuoso instance
for query in "${QUERIES[@]}"; do
    # Measure the execution time of the query
    start_time=$(date +%s%3N)

    # Execute the query using curl to the Virtuoso SPARQL endpoint
    result=$(curl -s -X POST \
        --data-urlencode "query=${query}" \
        http://localhost:8890/sparql)

    # End time after the query execution
    end_time=$(date +%s%3N)

    # Calculate the time difference
    execution_time=$((end_time - start_time))

    # Write the query and execution time to the CSV file
    echo "\"${query}\",${execution_time}" >> $output_file
done

echo "Execution times saved to ${output_file}"
