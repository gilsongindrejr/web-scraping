import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/Mouse-Gamer-Logitech-G502-LIGHTSPEED/dp/B07DCSZV9Y/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3PPPLWB72E60Q&keywords=logitech+g502&qid=1641912312&s=computers&sprefix=logitech+g502%2Ccomputers%2C254&sr=1-3&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

r = requests.get(url=url, headers=headers)

html = r.content.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

price_whole = soup.find_all('span', class_='a-price-whole')[0].text
price_fraction = soup.find_all('span', class_='a-price-fraction')[0].text

price = price_whole + price_fraction

print(price)

