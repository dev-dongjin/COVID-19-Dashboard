import chroller as chrol
from bs4 import BeautifulSoup


def readFile():
    print()

def saveFile(soup):
    # 국가 파일 만들기
    country_text = open('//Users/dongjinlee/programming/js/sandbox/python/tsotry/국가.txt', 'w')
    # 확진자 수 파일 만들기
    number_text = open('//Users/dongjinlee/programming/js/sandbox/python/tsotry/확진자수.txt', 'w')

    # 순서대로 국가 정보 가져오기
    countries = soup.find(id='main_table_countries_today').find_all("a", attrs={"class": "mt_a"}, limit=50)

    # 날짜와 전세계 확진자수 저장
    country_text.write(chrol.us+'\n')
    country_text.write('world'+'\n')
    number_text.write(chrol.kr+'\n')
    number_text.write(chrol.t+'\n')

    # 파일 쓰기
    for country in countries:
        country_text.write(country.text+'\n')
        number_text.write(country.find_next("td").text+'\n')
    
    # 파일 닫기
    country_text.close()
    number_text.close()
  

def editHTML():
    content = open("//Users/dongjinlee/programming/js/sandbox/python/tsotry/content.html")
    soup = BeautifulSoup(content, 'html.parser')
    all_ids = soup.find_all(id=True)
    print(all_ids)

    for id in all_ids:
        id.string="ssss"


    new_content = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/new_content[{chrol.us}].html', 'w')
    new_content.write(str(soup))

    content.close()
    new_content.close()
    
    
    
    
    # # 보낼 파일 열기


    # with open("//Users/dongjinlee/programming/js/sandbox/python/tsotry/content.html", 'r') as content:
        # soup = BeautifulSoup(content, 'html.parser')
        # all_ids = soup.find_all(id=True)
        # print(all_ids)

    #     # for id in all_ids:
    #     #     id.string="ssss"

    #     # print(all_ids)

    #     test = content.read()

    #     print(test)
    #     print("klsdkjfl")
    #     new_content = open('//Users/dongjinlee/programming/js/sandbox/python/tsotry/new_content.txt', 'w')

        
    #     

    #     new_content.close()



# <span id="kr"></span>, <span id="us"></span>, <span id="kr1"></span>, <span id="kr2"></span>, <span id="0"></span>, <span id="t"></span>, <span id="1"></span>, <span id="2"></span>, <span id="3"></span>, <span id="4"></span>, <span id="5"></span>, <span id="6"></span>, <span id="7"></span>, <span id="8"></span>, <span id="9"></span>, <span id="10"></span>, <span id="11"></span>, <span id="12"></span>, <span id="13"></span>, <a href="" id="p"></a>

