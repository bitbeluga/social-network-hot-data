from bs4 import BeautifulSoup
import requests
from datetime import datetime

print("\n""\n""Baidu start_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

url = "https://top.baidu.com/board?tab=realtime"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

data = soup.select(
    '#sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div')
for item in data:
    result = {
        'rank': item.select('div.content_1YWBm > a')[0].get_text(),
        'link': item.select('div.content_1YWBm > a')[0].get('href'),
        'hotCount': item.select('div.trend_2RttY.hide-icon > div.hot-index_1Bl1a')[0].get_text(),
    }
    print(result)
print("Baidu end_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
