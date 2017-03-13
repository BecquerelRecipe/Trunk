from bs4 import BeautifulSoup
import requests

url = "www.marmiton.org/recettes/recette_galette-des-rois_10832.aspx"

r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))