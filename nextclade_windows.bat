set input=%1
set batch=%2

C:\Users\KMB\nextclade dataset get --name sars-cov-2 --output-dir data/sars-cov-2

C:\Users\KMB\nextclade run --input-dataset data/sars-cov-2 --output-all="C:\Users\KMB\TomasC\output" --output-csv=%batch%.txt --output-basename=%batch% %input%
