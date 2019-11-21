import bs4
import requests
import re
from requests.exceptions import \
    MissingSchema, InvalidSchema, SSLError, ConnectionError, ReadTimeout
from multiprocessing import Pool

def crawlPage(link):
    try:
        r = requests.get(link, timeout=10)
        bs = bs4.BeautifulSoup(r.content, 'html.parser')
        notVisited = []
        for newLink in bs.find_all('a'):
            newLinkStr=str(newLink.get('href'))
            # if re.match("/", newLinkStr):
            #     newLinkStr=link+newLinkStr
            if re.match("http|www", newLinkStr):
                notVisited.append( newLinkStr )
        return( link, r.content, notVisited )
    except (MissingSchema, InvalidSchema, SSLError, ConnectionError, ReadTimeout):
        pass


def crawl(start_page, distance, action):
    notVisited = [start_page]
    visited = []
    for i in range(distance):
        print( 'distance: ', i+1 ,'/', distance)
        p = Pool(100)
        toVisit = [i for i in notVisited if i not in visited]
        toVisit = list(set(toVisit)) 
        result = p.map(crawlPage, toVisit)
        visiting = []
        print( len(result) )
        for r in result:
            if r is not None:
                link, content, newLink = r
                if link not in visited:
                    yield (link, action(content))
                visiting.extend(newLink)
        visited.extend(notVisited)
        notVisited.extend(visiting)

def findPython(text):
    result = []
    for sentence in text.decode(errors='ignore').replace('<','. ').replace('>','. ').split(". "):
        if re.search("Python", sentence):
            result.append(sentence)
    return result

url = 'http://www.ii.uni.wroc.pl'
url = 'https://www.onet.pl'
result = []
for i in crawl(url, 2, findPython):
    print( i )
    result.append( i )
print( '# result:\t', len([i[0] for i in result]) )
print( '# unique result:', len(set([i[0] for i in result])) )
