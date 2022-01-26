import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

connection = MongoClient('mongodb+srv://rangocerto:rightfood@cluster0.tljy8.mongodb.net/rightFood?retryWrites=true&w=majority')
database = connection.cooks
collection = database.cooking_recipes


receitas = collection.find()
for item in receitas:
    print(item)