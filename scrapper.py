import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

connection = MongoClient('mongodb+srv://rangocerto:rightfood@cluster0.tljy8.mongodb.net/rightFood?retryWrites=true&w=majority')
database = connection.cooks
collection = database.cooking_recipes

for i in range(1,99):
    xmlReceitas = requests.get(f"https://www.tudogostoso.com.br/sitemap-{i}.xml").content
    receitas = BeautifulSoup(xmlReceitas, 'xml')

    listaReceitas = receitas.find_all("loc")
    cooker = []
    for receita in listaReceitas:
        html = requests.get(receita.get_text()).content

        soup = BeautifulSoup(html, 'html.parser')

        titulo = soup.find("div", class_="recipe-title").find('h1')

        print(titulo.get_text())

        ingredientes = soup.find_all("span", class_="p-ingredient")

        # print('Ingredientes:')
        ingredients = []
        for ingrediente in ingredientes:
            ingredients.append(ingrediente.get_text().replace("\n", ""))

        # print('\n')
        # print('Preparo:')
        instructions = []
        instrucoes = soup.find("div", class_="instructions e-instructions").find('ol').find_all('li')
        for preparo in instrucoes:
            instructions.append(preparo.find('span').get_text().replace("\n", ""))

        # cooker.append({
        #     "title": titulo,
        #     "ingredients": ingredients,
        #     "instructions": instructions
        # })
        
        hasTitle = collection.count_documents({"title": titulo.get_text().replace("\n", "")})
        if not hasTitle:
            inserted = collection.insert_one({
                "title": titulo.get_text().replace("\n", ""),
                "ingredients": ingredients,
                "instructions": instructions
            })