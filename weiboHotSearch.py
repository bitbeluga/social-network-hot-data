from bs4 import BeautifulSoup
import requests

url = 'https://s.weibo.com/top/summary/summary?cate=realtimehot'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href')
    }
    print(result)
