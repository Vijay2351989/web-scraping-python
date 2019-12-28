import requests
from bs4 import BeautifulSoup
import pprint
import sys

pages = int(sys.argv[1])

fullList = []


def get_score(subtext):
    score = subtext.select(".score")
    if(score):
        return int(score[0].get_text().replace(' points', ''))
    else:
        return 0


def create_custom_hn(links, votes):
    hn = []
    for id, item in enumerate(links):
        title = item.get_text()
        href = item.get('href', None)
        score = get_score(subtexts[id])
        if(score > 100):
            hn.append({'title': title, 'link': href, 'score': score})
    return hn


for i in range(pages):
    response = requests.get(f'https://news.ycombinator.com/news?p={i+1}')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.storylink')
    subtexts = soup.select('.subtext')
    fullList.extend(create_custom_hn(links, subtexts))

fullList.sort(key=lambda k: k['score'], reverse=True)

pprint.pprint(fullList)
