import pdfkit

import bs4
import requests
import re

def download(url, file):
    """
    **Download url content to file**
    This downloads data and saves it with provided file name
    """
    options = {
    'quiet': '',
    'javascript-delay': 1000,
    }
    pdfkit.from_url(url, file, options=options)

def get_title(url):
    """
    **Returns title of webpage**
    This loads web page based on url and return it title
    """
    #This retrieves the webpage content
    r = requests.get(url)
    bs = bs4.BeautifulSoup(r.content, 'html.parser')
    #This parses the content
    title = bs.find('title').text
    return title

def worker(q,s):
    """
    **Download threads**
    This is threads for asynchronic content downloading 
    """
    while True:
        item = q.get()
        if item is None:
            break
        (id, url) = item
        s.put((id, 'Downloading'))
        try:
            title = get_title(url)
            download(url, '../data/'+title+'.pdf')
            s.put((id, 'Downloaded'))
        except OSError:
            s.put((id, 'Downloaded'))
        except  Exception as e:
            s.put((id, e))
        finally:
            q.task_done()

