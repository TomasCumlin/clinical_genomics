set input=%1
set batch=%2

nextclade dataset get --name sars-cov-2 --output-dir data/sars-cov-2

nextclade run --input-dataset data/sars-cov-2 --output-all=cd --output-csv=%batch%.txt --output-basename=%batch% %input%
