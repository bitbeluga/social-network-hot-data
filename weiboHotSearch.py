import re

from bs4 import BeautifulSoup
import requests

url = 'https://s.weibo.com/top/summary/summary?cate=realtimehot'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02')
for item in data:
    span = item.select("span")
    hotCount = 0
    for sp in span:
        hotCount = sp.get_text()
    if hotCount == 0:
        continue
    result = {
        'hotCount': hotCount,
        'title': item.select("a")[0].get_text(),
        'link': item.select("a")[0].get('href'),
    }
    print(result)
