from bs4 import BeautifulSoup
import requests
from datetime import datetime

print("\n""\n""Zhihu start_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

url = 'https://www.zhihu.com/billboard'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

data = soup.select(
    '#root > div > main > div > a > div.HotList-itemBody')
for item in data:
    result = {
        'title': item.select('.HotList-itemTitle')[0].get_text(),
        'hotCount': item.select('.HotList-itemMetrics')[0].get_text(),
    }
    print(result)

print("Zhihu end_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
