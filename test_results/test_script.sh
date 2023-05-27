#!/bin/bash

# An array of concurrency levels to test
concurrency_levels=(1 10 100)

# An array of total request numbers to test
total_requests=(100 1000 10000)

# Number of times to run each test
runs=5

# Delay between each test run
delay=15

# File to store the summary of the results
summary_file="summary.txt"

# Clear the summary file
echo "" > $summary_file

# Loop over all combinations of concurrency level, total requests, and number of runs
for c in "${concurrency_levels[@]}"; do
    for n in "${total_requests[@]}"; do
        for r in $(seq 1 $runs); do
            # Log file for this test run
            log_file="ab_c${c}_n${n}_run${r}.log"

            # Run the test and log the output
            ab -n $n -c $c http://localhost:5001/fetch_data > $log_file

            # Extract key metrics and write them to the summary file
            echo "Concurrency: $c, Total requests: $n, Run: $r" >> $summary_file
            grep 'Time taken for tests:' $log_file >> $summary_file
            grep 'Transfer rate:' $log_file >> $summary_file
            grep 'Total transferred:' $log_file >> $summary_file
            grep 'Requests per second:' $log_file >> $summary_file
            echo "" >> $summary_file

            # Wait before the next test run
            sleep $delay
        done
    done
done
