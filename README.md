# clinical_genomics

# Functioning nextclade files:

## Completed gplugin files ready to use:
        Linux: nextclade_linux_1.0.gplugin

## For Linux (using bash and shell):
        nc_code_bash.sh is to be used as plugin in Geneious  
        nc_code_bash.sh runs nextclade.sh, which is where all nextclade commands are located.

## For Windows (using batch):
        nextclade_windows.bat

 ### Python version:
        Linux: nextclade.py
        Windows: nextclade_windows.py & nextclade_windows_python.bat 
        
        The python-files for Linux and Windows are almost the same, besides these differences:
        * nextclade_windows.py must be run via nextclade_windows_python.bat. I.e. nextclade_windows_python.bat is used as plugin in Geneious
        * Paths need to be updated for each individual computer
        * nextclade_windows.py uses .replace("\n", "") for the nextclade version in order for nextclade_final.tsv to display columns correctly.



## Old files, not to be used: 
        nextclade_september.py
  


# Updated 2022-12-13
