# import libraries
import requests
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://wybory.gov.pl/sejmsenat2019/pl/wyniki/komitet/26079/sejm/pl'

page = requests.get(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.content, 'html.parser')
# print( soup )
# Take out the <div> of name and get its value
name_box = soup.find_all('table', {"id": "DataTables_Table_11"})
name_box = soup.find_all(id="DataTables_Table_11")
# name = name_box.text.strip() # strip() is used to remove starting and trailing
print( name_box )
for i in name_box:
    print( i )