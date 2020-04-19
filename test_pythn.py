import telegram
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from apscheduler.schedulers.blocking import BlockingScheduler


token = '1001744474:AAEYkSP8P9mIUcsPT_Pzx8pPIbKpuw1Pr_8'
bot = telegram.Bot(token=token)
sched = BlockingScheduler()


def selenium_test():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path="/home/ubuntu/settings/geckodriver/geckodriver")
    driver.get("http://google.com/")
    print(driver.title)
    driver.quit()   

def chatBot():
    print("chatBot")
    bot.sendMessage(chat_id='1020617783', text="URL")
    print("chatBot 완료")



# 최초 1회 시작
# chatBot()

# 시간마다 반복시키기
# sched.add_job(start, 'interval', hours=24)

print("시작")
sched.add_job(chatBot,'cron', hour=20, minute=4)

sched.start()


