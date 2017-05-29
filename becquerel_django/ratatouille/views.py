import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

from . import webparser
from . import retrieve_ingredients


def index(request):
    return HttpResponse("Ratatouille says hello world!")


def scraper_launch(request, urlToScrap):
    html_text = requests.get(urlToScrap).text
    soup = BeautifulSoup(html_text, 'html.parser')
    soup.prettify()

    recipeFilter = "m_content_recette_ingredients m_avec_substitution"
    ingredients = soup.find('div', {'class': recipeFilter})
    # print(ingredients.text)
    a = ingredients.text
    ingredients_rev = a.replace('\n', ' ')
    # print(ingredients_rev)
    parsed_ingredients = webparser.ingredients_parser(ingredients_rev)

    return HttpResponse(parsed_ingredients)

def test_retrieve(request, urlToScrap):
    html_text = requests.get(urlToScrap).text
    soup = BeautifulSoup(html_text, 'html.parser')
    soup.prettify()

    recipeFilter = "m_content_recette_ingredients m_avec_substitution"
    ingredients = soup.find('div', {'class': recipeFilter})
    # print(ingredients.text)
    a = ingredients.text
    ingredients_rev = a.replace('\n', ' ')
    # print(ingredients_rev)
    parsed_ingredients = webparser.ingredients_parser(ingredients_rev)

    test = retrieve_ingredients.retrieve(parsed_ingredients)
    return HttpResponse(test)
