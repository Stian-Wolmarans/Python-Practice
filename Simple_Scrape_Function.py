import requests
from bs4 import BeautifulSoup

# get url and or page to search
search_url = input("Search website: ")

#get html of webpage
r = requests.get(search_url)
soup = BeautifulSoup(r.content, 'html.parser')

#specifiy search
result = soup.find('img', {'width' : '260'})['src']
print(result)