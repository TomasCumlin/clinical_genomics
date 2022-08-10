# To run: < .\nextclade_windows.ps1 input_path.fasta batch_name

$input=$args[0]
$batch=$args[1]

nextclade dataset get --name 'sars-cov-2' --output-dir 'data/sars-cov-2'

nextclade run \
   --input-dataset data/sars-cov-2 \
   --output-all=output/ \
   --output-csv=output/$batch.csv
   --output-basename=$batch
 $input