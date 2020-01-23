import pdfkit

import bs4
import requests
import re

def download(url, file):
    pdfkit.from_url(url, file)

def get_title(url):
    #This retrieves the webpage content
    r = requests.get(url)
    bs = bs4.BeautifulSoup(r.content, 'html.parser')
    #This parses the content
    title = bs.find('title').text
    return title

def worker(q,s):
    while True:
        item = q.get()
        if item is None:
            break
        (id, url) = item
        s.put((id, 'Downloading'))
        try:
            title = get_title(url)
            download(url, 'data/'+title+'.pdf')
            s.put((id, 'Downloaded'))
        except  Exception as e:
            s.put((id, str(e)))
            # print("An exception occurred")
        finally:
            q.task_done()

