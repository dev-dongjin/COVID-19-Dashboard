import chroller as chrol
from bs4 import BeautifulSoup
from googletrans import Translator


def y_readFile():
    country_text = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/국가[{chrol.previous_date}].txt', 'r')
    number_text = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/확진자수[{chrol.previous_date}].txt', 'r')
    info = {}

    country_lines = country_text.readlines()
    for c_line in country_lines:
        n_line = number_text.readline()
        c = c_line.replace('\n','')
        n = n_line.replace('\n','')
        info[f"{c}"] = [c, n]
    country_text.close()
    number_text.close()
    
    print(info["USA"])
    print(info["USA"][0])
    print(info["USA"][1])


    return info

def t_readFile():
    country_text = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/국가[{chrol.kr}].txt', 'r')
    number_text = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/확진자수[{chrol.kr}].txt', 'r')
    info = []

    country_lines = country_text.readlines()
    for c_line in country_lines:
        n_line = number_text.readline()
        c = c_line.replace('\n','')
        n = n_line.replace('\n','')
        info.append([c, n])
    country_text.close()
    number_text.close()
    
    print(info[0])
    print(info[0][0])
    print(info[0][1])

    return info

def saveURL(url):
    saveURL = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/URL[{chrol.kr}].txt', 'w')
    saveURL.write(url)
    saveURL.close()


def readURL():
    print(chrol.previous_date)
    readURL = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/URL[{chrol.previous_date}].txt', 'r')
    url = readURL.readline()
    print(url)
    readURL.close()  
    return url  


def saveFile(soup):
    # 국가 파일 만들기
    country_text = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/국가[{chrol.kr}].txt', 'w')
    # 확진자 수 파일 만들기
    number_text = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/확진자수[{chrol.kr}].txt', 'w')

    

    # 순서대로 국가 정보 가져오기
    countries = soup.find(id='main_table_countries_today').find_all("a", attrs={"class": "mt_a"}, limit=50)
    
    # 한국 인덱스 찾기
    i = 0
    for coun in countries:
        find_korea = coun.text
        if(find_korea == "S. Korea"):
            break
        i = i + 1
    print(i)
    
    # 날짜와 전세계 확진자수 저장
    country_text.write(chrol.us+'\n')
    country_text.write('World'+'\n')
    number_text.write(chrol.kr+'\n')
    number_text.write(chrol.t+'\n')

    # 파일 쓰기
    count = 0
    for country in countries:
        country_text.write(country.text+'\n')
        number_text.write(country.find_next("td").text+'\n')
        count = count + 1
        if count>i:
            break
    
    # 파일 닫기
    country_text.close()
    number_text.close()
  

def editHTML(list):
    content = open("//Users/dongjinlee/programming/js/sandbox/python/tsotry/content.html")
    soup = BeautifulSoup(content, 'html.parser')
     
    y_info = y_readFile()
    t_infos = t_readFile()

    # 날짜 추가
    us_date = soup.find(id="0")
    us_date.string = t_infos[0][0]
    for i in range(4):
        date = soup.find(id=f"kr{i}")
        date.string = t_infos[0][1]

    # 전세계 확진자 수 추가
    t = soup.find(id="t")
    t.string = t_infos[1][1]
    tn = soup.find(id="tn")
    tn.string = str((int(str(t_infos[1][1]).replace(",",""))-int(str(y_info["World"][1]).replace(",",""))))

    #대한민국 확진자 수 추가
    korea = len(t_infos)-1
    t = soup.find(id="k")
    t.string = t_infos[korea][1]
    tn = soup.find(id="kn")
    tn.string = str((int(str(t_infos[korea][1]).replace(",",""))-int(str(y_info["S. Korea"][1]).replace(",",""))))


    # 나라별 확진자 수 추가
    for i in range(7):
        country_name = soup.find(id=f"{i}")
        if (i>1) :
            country_name.string=translate(t_infos[i][0])
        
        country_number = soup.find(id=f"{i}n")
        if (i>1) :
            country_number.string=str(int(str(t_infos[i][1]).replace(",",""))-int(str(y_info[t_infos[i][0]][1]).replace(",","")))

    # 전일의 값
    y = soup.find(id="y")
    y.string = chrol.previous_date
    p = soup.find(id="p")
    print(p)
    url = readURL()
    p['href'] = url
    p.string = url


    print("START!!!!!!!!!")

    # 사진넣기
    for i in range(3):
        img_tags = soup.find_all(attrs={"class": f'{i}'})
        img_tags[0]['data-url'] = list[i]
        img_tags[0].contents[1]['src'] = list[i]
        i = i +1        

    new_content = open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/new_content[{chrol.kr}].html', 'w')
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

def translate(word):
    translator = Translator()
    result = translator.translate(word, dest="ko")
    print(result.text)
    return str(result.text)