import json
from bs4 import BeautifulSoup
import requests
import re

url = 'https://d.weibo.com/231650'
headers = {
    'Postman-Token': '',
    'Host': '',
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.select(
    '#page > div.c-d.c-d-e > div.Zd-p-Sc > div:nth-child(1) > div.cc-dc-c > div > div.jc-c > table > tbody > tr > td.al > a')
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href')
    }
    print(result)
