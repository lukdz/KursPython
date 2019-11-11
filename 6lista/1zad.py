import bs4
# from bs4 import BeautifulSoup
import requests
import re

def search(start_page, distance):
    if distance > 0:
        try:
            r = requests.get(start_page)
            bs = bs4.BeautifulSoup(r.content, 'html.parser')
            yield (start_page, r.content)
            for link in bs.find_all('a'):
                if re.match("/", link.get('href')):
                    yield from search(start_page+link.get('href'), distance-1)
                else:
                    yield from search(link.get('href'), distance-1)
        except:
            pass
            # yield start_page


def crawl(start_page, distance, action):
    for link, page in set(search(start_page, distance)):
        yield (link, action(page))


url = 'http://www.ii.uni.wroc.pl'
result = []
for i in crawl(url, 2, len):
    print( i )
    result.append( i )
print( len(result) )
print( len(set(result)) )
