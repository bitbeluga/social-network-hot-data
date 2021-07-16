from bs4 import BeautifulSoup
import requests
from datetime import datetime

print("\n""\n""Toutiao start_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

url = "https://tophub.today/n/x9ozB4KoXb"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
data = soup.select(
    '#page > div.c-d.c-d-e > div.Zd-p-Sc > div:nth-child(1) > div.cc-dc-c > div > div.jc-c > table > tbody')
for item in data:
    print(item.select('tr > td')[3].get_text())
    result = {
        'rank': item.select('tr > td')[0].get_text(),
        'title': item.select('tr > td.al > a')[0].get_text(),
        'hotCount': item.select('tr > td')[2].get_text(),
    }
    print(result)
#
# print("Zhihu end_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
