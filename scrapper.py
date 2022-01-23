from bs4 import BeautifulSoup
import requests

xml = requests.get('https://www.tudogostoso.com.br/sitemap-1.xml').content
receitas = BeautifulSoup(xml, 'xml')

listaReceitas = receitas.find_all("loc")
for receita in listaReceitas:
    print(receita.get_text())

    html = requests.get(receita.get_text()).content

    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.prettify())

    titulo = soup.find("span", class_="current")

    print(titulo.get_text())

    ingredientes = soup.find_all("span", class_="p-ingredient")

    print('Ingredientes:')
    for ingrediente in ingredientes:
        print(ingrediente.get_text())

    print('\n')
    print('Preparo:')
    preparos = soup.find_all("div", class_="instructions e-instructions")
    for preparo in preparos:
        print(preparo.get_text())