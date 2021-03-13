import requests
from bs4 import BeautifulSoup

joblist = []

def extract(pages):
    i = 10
    url = f'https://fr.indeed.com/jobs?q=cloud&l=%C3%8Ele-de-France&sort=date&start={pages}'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    #a supp
    transform(soup)
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ ='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        compagny = item.find('span', class_ ='company').text.strip()

        try:
            salary = item.find('span', class_ = 'salaryText').text.strip()
        except:
            salary = '$'
        summary = item.find('div', class_ = 'summary').text.strip().replace('\n','')
        
        lk = item.get('data-jk')
        link = f'https://fr.indeed.com/voir-emploi?jk={lk}'
        
        city = item.get('data-rc-loc')

        job = {
            'title': title,
            'company': compagny,
            'salary': salary,
            'summary': summary,
            'link': link,
            'city': city,
            'idjob': lk
        }
        joblist.append(job)
        
    return joblist

extract(0)