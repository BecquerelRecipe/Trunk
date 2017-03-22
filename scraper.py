from bs4 import BeautifulSoup
import requests
from huh import ingredients_parser as parse
url = "www.marmiton.org/recettes/recette_galette-des-rois_10832.aspx"

r = requests.get("http://" +url)

data = r.text


soup = BeautifulSoup(data, 'html.parser')
#print(soup.prettify())

name = "m_content_recette_ingredients m_avec_substitution"
ingredients = soup.find('div', {'class': name})
#print(ingredients.text)
a = ingredients.text
ingredients_rev = a.replace('\n',' ')
#print(ingredients_rev)
parse(ingredients_rev)

#for link in soup.find_all('a'):
#    print(link.get('href'))