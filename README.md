# COVID-19 Dashboard

> This bot automatically updates your [Tistory](https://www.tistory.com/) blog with the daily count of COVID-19 cases worldwide, providing an easy-to-read overview of the data.

## Features

1. At midnight KST (Korean Standard Time) every day, the bot scrapes data from the [source](https://www.worldometers.info/coronavirus/).
2. It retrieves the image of global COVID-19 cases and the top 6 countries with the highest number of cases, along with the counts for South Korea and Japan.
3. The bot then posts this information on your connected Tistory blog.
4. Once the posting is complete, it sends a notification to your linked Telegram account.

## Technology used

- Python3
- BeautifulSoup
- Selenium
- python-telegram-bot
- Tistory Open API

## Example

### Tistory Blog

<center><img src="https://user-images.githubusercontent.com/39150608/126060601-6dcb227c-b7e4-4e43-b47a-97332f5a299b.png" width="500"></center>

### Telegram Message

<center><img src="https://user-images.githubusercontent.com/39150608/126060641-c1b65cd2-3a14-4889-ab1a-5a2cd9d71f98.png" width="500"></center>

[Example Blog](https://digitalnomad-lee.tistory.com/546?category=850377)
