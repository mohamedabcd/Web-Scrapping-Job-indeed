import requests
from bs4 import BeautifulSoup

joblist = []

def extract(pages):
    i = 10
    url = f'https://fr.indeed.com/jobs?q=cloud&l=%C3%8Ele-de-France&sort=date&start={pages}'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup