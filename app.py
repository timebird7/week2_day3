from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("nice to meet you")
    return """
    <h1>깨굴</h1>
    <img src="data:image/jpeg;base64,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">
    <h3>Hello world</h3>
    """

@app.route('/naver_toon')
def naver_toon():


    today = time.strftime("%a").lower()
    print(today)
    # 네이버 웹툰을 가져올 수 있는 주소url을 파악한다.
    # url 변수에 저장한다.
    # 해당 주소로 요청을 보내 정보를 가져온다.
    # 받은 정보를 bs를 이용해 검색하기 좋게 만든다
    # 네이버 웹툰 페이지로 가서, 내가 원하는 정보가 어디에 있는지 파악한다.

    url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=tue'
    response = requests.get(url).text
    soup = bs(response, 'html.parser')

    toons = []
    li = soup.select('.img_list li')
    for item in li:
        toon = {
        'title' : item.select_one('dt a').text,
        'url' : item.select('dt a')[0]['href'],
        'img_url' : item.select('.thumb img')[0]['src']
        }
        
        toons.append(toon)
  
    return render_template('naver_toon.html', t = toons)
       
@app.route('/daum_toon')
def daum_toon():
    return render_template('naver_toon.html')