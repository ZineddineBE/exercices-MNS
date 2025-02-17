from pymongo import MongoClient
import mysql.connector
from faker import Faker
import os

fake = Faker(locale="fr_FR")

mongo_client = MongoClient('mongodb://localhost:27017/')

mysql_client = mysql.connector.connect(
    user='root', 
    password='',
    host='localhost',
    database='test_db'
)

# Génération de 1000 000 000 000 de nom et prénom

for i in range(1000000000):
    
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    # Insertion dans MongoDB
    mongo_db = mongo_client['test_db']
    mongo_collection = mongo_db['people']
    mongo_collection.insert_one({'first_name': first_name, 'last_name': last_name})
    
    # Insertion dans MySQL
    cursor = mysql_client.cursor()
    query = f"INSERT INTO people (first_name, last_name) VALUES ('{first_name}', '{last_name}')"
    cursor.execute(query)
    mysql_client.commit()