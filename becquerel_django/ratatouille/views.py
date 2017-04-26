from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .webparser.webparser import ingredients_parser as parse

def index(request):
    return HttpResponse("Ratatouille says hello world!")


def scraper_launch(request, urlToScrap):
    html_text = requests.get(urlToScrap).text
    soup = BeautifulSoup(html_text, 'html.parser')
    html_to_parse = soup.prettify()

    recipeFilter = "m_content_recette_ingredients m_avec_substitution"
    ingredients = soup.find('div', {'class': recipeFilter})
    # print(ingredients.text)
    a = ingredients.text
    ingredients_rev = a.replace('\n', ' ')
    # print(ingredients_rev)

    return HttpResponse(parse(ingredients_rev))
