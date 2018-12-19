import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/'
response = req.get(url).text

soup = bs(response, 'html.parser')

kospi = soup.select('.num')[0].text

print("현재 코스피 지수 : {}".format(kospi))      