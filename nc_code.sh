# this sh-file is to be run by nc_code_bash.sh in order to activate the environment correctly.
# Therefore, run nc_code_bash.sh in the terminal, not this file.


conda activate /home/ete03/miniconda3/envs/nextclade_new


nextclade run \
   --input-dataset '/home/ete03/Documents/pangolin_testing/output/nextclade_new_env/data/sars-cov-2' \
   --output-all='/home/ete03/.geneious2022.1data/transient/1657871809796/x/' \
   --output-csv=$2.txt \
   --output-basename=$2 \
   $1

