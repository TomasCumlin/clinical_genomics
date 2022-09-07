import os
import sys
import json

#print current nextclade version

os.system("nextclade --version")

#open the json-file
f = open('tag.json')

#convert the json-file to a dict
data = json.load(f)

#print the version of the database
print(("Database version: {}").format(data['tag']))
  
# Closing file
f.close()