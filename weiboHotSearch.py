
import requests
from bs4 import BeautifulSoup
from datetime import datetime

print("\n""\n""WeiboHotSearch start_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

url = 'https://s.weibo.com/top/summary/summary?cate=realtimehot'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
data = soup.select('#pl_top_realtimehot > table > tbody > tr')

for item in data:
    rankTd = item.select("td.td-01.ranktop")
    rank = 0
    for td in rankTd:
        rank = td.get_text()
    hotCountSpan = item.select("td.td-02 > span")
    hotCount = 0
    for sp in hotCountSpan:
        hotCount = sp.get_text()
    if hotCount == 0 or hotCount == '':
        continue
    result = {
        'rank': rank,
        'count': hotCount,
        'title': item.select("td.td-02 > a")[0].get_text(),
        'url': 'https://s.weibo.com/' + item.select("td.td-02 > a")[0].get('href'),
    }
    print(result)

print("WeiboHotSearch end_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
