from bs4 import BeautifulSoup
import requests

url = 'https://tophub.today/n/K7GdaMgdQy'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text)
data = soup.select(
    '#page > div.c-d.c-d-e > div.Zd-p-Sc > div:nth-child(1) > div.cc-dc-c > div > div.jc-c > table > tbody > tr > td.al > a')
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href')
    }
    print(result)
