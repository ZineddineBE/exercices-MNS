from pymongo import MongoClient
import re
# Requires the PyMongo package.
# https://api.mongodb.com/python/current
client = MongoClient('mongodb://localhost:27017/')

filter={}

stagiaires = client['dw1']['stagiaires'].find(
  filter=filter,
  limit=5,
  sort=['nom']
)

for stagiaire in stagiaires:
    print(f"Id: {stagiaire["_id"]}\nNom: {stagiaire["nom"].upper()}\nPrénom: {stagiaire["prenom"]}\n")
    