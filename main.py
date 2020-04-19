import tstory as tistory
import chroller as chrolling
import file_handling as file_handle
import element_capture as cap
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


print("Start")
sched = BlockingScheduler()


def start():
    chrolling.extract_links()

    # 사진다운로드 받기(완료)
    print("Test")
    cap.capture()

    list = []

    # 사진올리기(완료)
    tistory.init()
    i = 0
    for i in range(3):
        i = i +1
        list.append(tistory.file_write(f'my_screenshot_name{i}'))

    # 블로그 올릴 내용 수정하기
    file_handle.editHTML(list)

    #파일읽고 텍스트화 시키기.(완료)
    with open(f'./data/new_content[{chrolling.kr}].html', 'r', encoding='utf-8') as file1:
        new_content = file1.read()

    #티스토리 글쓰기(완료)
    URL = tistory.get_write(new_content)
    print("start 완료")
    chatBot(URL)
    


def chatBot(URL):
    print("chatBot")
    token = '1001744474:AAEmsYJu9KHxb8Iza4d0OfHw2kpPE7BXZg4'
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id='1020617783', text=URL)
    print("chatBot 완료")



# 최초 1회 시작
start()

# 시간마다 반복시키기
# sched.add_job(start, 'interval', hours=24)
sched.add_job(start,'cron', hour=5)

# 시작
sched.start()
print("완료")
#티스토리 직전파일 읽어오기.
# tstory.get_read()



# print(new_content)

# 티스토리 메소드
# print('list의 첫번째 글'+tstory.get_list(1))
# tstory.get_read()
# tstory.get_category()


# # 첫번째 리스트의 값 들고오기
# new_list = tistory.get_list("1")

# # 리스트에서 post id찾기
# new_post_id = new_list.json()['tistory']['item']['posts'][0]['id']

# # post id로 포스트 가져오기
# new_post = tistory.get_read(new_post_id)

# # 포스트를 XML파일로 변환하기
# root = ET.fromstring(new_post.text)
# new_post_content = ''

# # 포스트에서 Content 내용 찾기
# for content in root.iter('content'):
#     new_post_content = content.text


# #파일읽고 텍스트화 시키기.(완료)
# with open(f'//Users/dongjinlee/programming/js/sandbox/python/tsotry/new_content[4월15일].html', 'r', encoding='utf-8') as file1:
#     new_content = file1.read()


# #티스토리 글쓰기(완료)

# tistory.get_write(new_content)

# tistory.init()
# tistory.get_category()
# exit()
# Worldometer 정보 가져오기(완료)