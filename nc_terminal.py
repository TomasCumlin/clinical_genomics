#!/home/ete03/anaconda3/bin/python

import os
import subprocess
import sys

infile=sys.argv[1]
batch_name=sys.argv[2]
output="/home/ete03/.geneious2022.1data/transient/1661157478899/x"

get_data="nextclade dataset get --name=sars-cov-2 --output-dir=data/sars-cov-2"
run_nextclade="nextclade run --input-dataset data/sars-cov-2 --output-all={} --output-tsv={}.tsv --output-basename={} {}".format(output, batch_name, batch_name, infile)

os.popen(get_data)

os.popen(run_nextclade)