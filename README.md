# 티스토리 자동 블로그 포스팅 봇 (전세계 코로나 확진자 수)
> 일별 전세계 코로나 확진자 수를 한눈에 볼 수 있게 티스토리 블로그에 자동으로 업데이트 해주는 봇입니다.
>  
> 한눈에 일별 확진자 수를 구분하여 보는게 어렵다고 생각이 들어 만들게 되었습니다.

## 작동 방식
1. 매일 한국시간(KST) 00시에 [출처](https://www.worldometers.info/coronavirus/)에서 스크래핑 동작을 실행합니다.
2. 전세계 확진자 수의 이미지와 국가별 확진자 수가 가장많은 순으로 1위에서 6위까지 및 한국, 일본의 확진자 수를 가져와 저장합니다.
3. 연결된 티스토리 블로그에 포스팅을 진행합니다. 
4. 포스팅이 완료가 되면 연결된 텔레그램으로 포스팅 완료 알람을 보냅니다.

## Tech used
- Python3
- BeautifulSoup
- Selenium
- python-telegram-bot
- 티스토리 Open API


## 예시
<블로그 이미지>
<center><img src="https://user-images.githubusercontent.com/39150608/126060601-6dcb227c-b7e4-4e43-b47a-97332f5a299b.png" width="500"></center>


<텔레그램 메세지>
<center><img src="https://user-images.githubusercontent.com/39150608/126060641-c1b65cd2-3a14-4889-ab1a-5a2cd9d71f98.png" width="500"></center>

[예시 블로그](https://digitalnomad-lee.tistory.com/546?category=850377)
