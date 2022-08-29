

import os
import subprocess
import sys

infile=sys.argv[1]      # The selected sequences to analyse in Geneious
batch_name=sys.argv[2]  # Name of the batch. Can be modified in Geneious.
output="C:/Users/KMB/TomasC/output"   # Path to where your results should be saved.
nextclade_path="C:/Users/KMB/nextclade"  # Path to where nextclade is installed.

get_data=[nextclade_path, "dataset", "get", "--name=sars-cov-2", "--output-dir=data/sars-cov-2"]
run_nextclade=[nextclade_path, "run", "--input-dataset", "data/sars-cov-2", "--output-all={}".format(output), "--output-tsv={}.tsv".format(batch_name), "--output-basename={}".format(batch_name), "{}".format(infile)]

output_dataset,error  = subprocess.Popen(
                    get_data, universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

output_results,error  = subprocess.Popen(
                    run_nextclade, universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()