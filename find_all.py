import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
database = connection.cooks
collection = database.cooking_recipes


receitas = collection.find()
for item in receitas:
    print(item)