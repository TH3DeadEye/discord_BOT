import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.ca/s?k=headphones&crid=1DS8GZM1STSD5&sprefix=headphones%2Caps%2C109&ref=nb_sb_noss_1'
page = requests.get(url=url).text
soup = BeautifulSoup(page, 'html.parser')
a = 4
for i in range (a):


    item_title = soup.find_all('span', id = 'B0C3HCD34R-amazons-choice')
    print(item_title)

