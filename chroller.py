from bs4 import BeautifulSoup
import requests
import file_handling as file


us = None
kr = None
t = 0


def extract_links():
    # 해당 url의 html문서를 soup 객체로 저장
    url = 'https://www.worldometers.info/coronavirus/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
   
    #날짜 값 가져오기
    getDate(soup)
    
    #한국 날짜 값 가져오기
    getKrDate(us)

    #전세계 확진자 수 가져오기.
    getTotal(soup)
   
    #국가별 확진자 정보 저장.
    file.saveFile(soup)


def getDate(soup):
     #날짜 값 가져오기
    last_updated = soup.find_all(attrs={"style": "font-size:13px; color:#999; margin-top:5px; text-align:center"})
    # 몇월 몇일(미국)
    global us
    us = last_updated[0].text.split(':')[1].split(',')[0].strip()

def getKrDate(us):
    # 한국날짜로 번역하기
    months = us.split(' ')[0]
    month = '4월'
    if months == 'April':
        month = '4월'
    elif months == 'May':
        month = '5월'
    # 몇월 몇일(한국)
    global kr
    kr = month+str(int(us.split(' ')[1])+1)+'일'
    print(kr)

def getTotal(soup):
    #전세계 확진자 수 가져오기.
    maincounter_number = soup.select('.maincounter-number')
    # 몇명(전세계)
    global t
    t = maincounter_number[0].select('span')[0].text


