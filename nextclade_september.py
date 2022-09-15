#!/home/ete03/anaconda3/bin/python

# This script runs the nextclade analysis on sequencing data. 
# It can either be directily run in the terminal (command: python nc_terminal.py <sequence data> <batch name>)
# or it can be used as a plugin in Geneious. 
# Variables path and nextclade_path must be updated before usage.

import os
import subprocess
import sys
import json
from datetime import date
import csv

today = str(date.today())

infile=sys.argv[1]      # The selected sequences to analyse in Geneious
batch_name=sys.argv[2]  # Name of the batch. Can be modified in Geneious.

# Update the path depending on where the data should be stored.
path="/home/ete03/Documents/clinical_genomics/"

# Path to where nextclade is installed.
nextclade_path="/home/ete03/miniconda3/bin/nextclade"

output=path+"output/"   #Path to where your results should be saved.

# Path to where you want to store your downloaded database.
# If you already have a database up-to-date, this step will be skipped.
database_path=path+"data/sars-cov-2/" 

get_data=[nextclade_path, "dataset", "get", "--name=sars-cov-2", "--output-dir=data/sars-cov-2"]
run_nextclade=[nextclade_path, "run", "--input-dataset", "data/sars-cov-2", "--output-all={}".format(output), "--output-tsv={}.tsv".format(batch_name), "--output-basename={}".format(batch_name), "{}".format(infile)]


output_dataset,error  = subprocess.Popen(
                    get_data, universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

output_results,error  = subprocess.Popen(
                    run_nextclade, universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# Save software and database info

#open the json-file
f = open(database_path+"tag.json")

#convert the json-file to a dict
data = json.load(f)

#r.write(("Database version: {}").format(data['tag']))

r = open("{}{}_final.csv".format(output, batch_name), 'w', newline='')
writer = csv.writer(r)

nextclade_vers = [nextclade_path, "--version"]
output_results2,error  = subprocess.Popen(
                nextclade_vers, universal_newlines=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

with open('{}{}.csv'.format(output,batch_name), 'r') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=";")
     for row in spamreader:
         if "seqName" in row[0]:
             row.append("Software version")
             row.append("Database version")
             writer.writerow(row)
         else:
             row.append(output_results2)
             row.append(data['tag'])
             writer.writerow(row)
         
f.close()
