import urllib.request
from bs4 import BeautifulSoup as bs
import requests
url =  'https://yandex.ru/pogoda/kazan'
page = requests.get(url)
print(page.status_code)
soup = bs(page.text, 'html.parser')
print(soup.prettify())
#print(soup.find('time', class_ = 'time fact__time' ).get_text())
print(soup.find('div', class_ = 'temp fact__temp fact__temp_size_s').get_text())
print(soup.find('div', class_ = 'link__condition day-anchor i-bem').get_text())
#print(soup.find('dt', class_ = 'term__label').get_text())
#print(soup.find('dd', class_ = 'term__value').get_text())
s = soup.find('div', class_ = 'fact__props fact__props_position_middle')
toda_wind_speed=s.find('span', class_="wind-speed").get_text()
today_wind_vect = s.find('abbr', class_ = 'icon-abbr').get_text()
today_humid = s.find('dl', class_ ='term term_orient_v fact__humidity').get_text()
today_pressur = s.find('dl', class_='term term_orient_v fact__pressure').get_text()
