import chroller as chrol
from bs4 import BeautifulSoup
from googletrans import Translator
# import make_chart as mkChart

rank_20 = None
japan_index = 0

def y_readFile():
    country_text = open(f'./data/국가[{chrol.previous_date}].txt', 'r')
    number_text = open(f'./data/확진자수[{chrol.previous_date}].txt', 'r')
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
    country_text = open(f'./data/국가[{chrol.kr}].txt', 'r')
    number_text = open(f'./data/확진자수[{chrol.kr}].txt', 'r')
    info = []
    count=0
    country_lines = country_text.readlines()
    for c_line in country_lines:
        n_line = number_text.readline()
        c = c_line.replace('\n','')
        n = n_line.replace('\n','')
        ##0503
        if(c=="Japan"):
            global japan_index
            japan_index=count
        count=count+1
        ##
        info.append([c, n])
    country_text.close()
    number_text.close()
    
    print(info[0])
    print(info[0][0])
    print(info[0][1])

    return info

def saveURL(url):
    saveURL = open(f'./data/URL[{chrol.kr}].txt', 'w')
    saveURL.write(url)
    saveURL.close()


def readURL():
    print(chrol.previous_date)
    readURL = open(f'./data/URL[{chrol.previous_date}].txt', 'r')
    url = readURL.readline()
    print(url)
    readURL.close()  
    return url  


def saveFile(soup):
    # 국가 파일 만들기
    country_text = open(f'./data/국가[{chrol.kr}].txt', 'w')
    # 확진자 수 파일 만들기
    number_text = open(f'./data/확진자수[{chrol.kr}].txt', 'w')
    print(chrol.kr)
    
    # 순서대로 국가 정보 가져오기
    countries = soup.find(id='main_table_countries_today').find_all("a", attrs={"class": "mt_a"}, limit=200)
    print(countries)
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

    chart_countries = []
    chart_numbers = []
    for country in countries:
        countryName = country.text
        number = country.find_next("td").text
        country_text.write(countryName+'\n')
        number_text.write(number+'\n')
        if(count<5):
            chart_countries.append(countryName)
            chart_numbers.append(int(number.replace(",","")))
        count = count + 1
        if count==19:
            global rank_20
            rank_20 = country.get('href')
        if count>i:
            break
    
    # 파일 닫기
    country_text.close()
    number_text.close()
  
    # mkChart.makeGraph(chart_numbers, chart_countries)
    # exit()


def editHTML(list):
    content = open("./data/content.html")
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

     #일본 확진자 수 추가
    japan = japan_index
    j = soup.find(id="j")
    j.string = t_infos[japan][1]
    jn = soup.find(id="jn")
    jn.string = str((int(str(t_infos[japan][1]).replace(",",""))-int(str(y_info["Japan"][1]).replace(",",""))))

    # 나라별 확진자 수 추가
    for i in range(8):
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
    # 5월 3일
    p.string = "2020년 "+chrol.previous_date+" 확진자 수"


    print("START!!!!!!!!!")

    # 사진넣기
    for i in range(3):
        img_tags = soup.find_all(attrs={"class": f'{i}'})
        img_tags[0]['data-url'] = list[i]
        img_tags[0].contents[1]['src'] = list[i]
        i = i +1        

    new_content = open(f'./data/new_content[{chrol.kr}].html', 'w')
    new_content.write(str(soup))

    content.close()
    new_content.close()

def translate(word):
    translator = Translator()
    result = translator.translate(word, dest="ko")
    print(result.text)
    return str(result.text)