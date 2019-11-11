import bs4
# from bs4 import BeautifulSoup
import requests
import re
from requests.exceptions import MissingSchema, InvalidSchema


def crawl(start_page, distance, action):
    notVisited = [(start_page,distance)]
    visited = []
    for link, distance in notVisited:
        if link not in visited and distance > 0:
            visited.append(link)
            try:
                r = requests.get(link)
                bs = bs4.BeautifulSoup(r.content, 'html.parser')
                yield ( link, action(r.content) )
                for newLink in bs.find_all('a'):
                    newLinkStr=str(newLink.get('href'))
                    if re.match("/", newLinkStr):
                        newLinkStr=link+newLinkStr
                    notVisited.append( (newLinkStr, distance-1) )
                # print( 'all links' )
            except (MissingSchema, InvalidSchema):
                pass

def findPython(text):
    # print( text )
    result = []
    for sentence in text.decode().replace('<','. ').replace('>','. ').split(". "):
    # for sentence in text.decode().split(". "):
        if re.search("Python", sentence):
            result.append(sentence)
            # print( sentence ) 
            # print( re.search("Python", sentence) ) 
    # return result[:1]
    return result

url = 'http://www.ii.uni.wroc.pl'
result = []
for i in crawl(url, 2, findPython):
    print( i )
    result.append( i )
# print( len(result) )
# print( len(set(result)) )
print( len([i[0] for i in result]) )
print( len(set([i[0] for i in result])) )
