from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def index(request):
    return HttpResponse("Ratatouille says hello world!")


def scraper_launch(request, urlToScrap):
    html_text = requests.get(urlToScrap).text
    soup = BeautifulSoup(html_text, 'html.parser')
    html_to_parse = soup.prettify()
    return HttpResponse(html_to_parse)
