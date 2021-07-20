from bs4 import BeautifulSoup
import requests

url = 'https://tophub.today/n/K7GdaMgdQy'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text)
data = soup.select(
    '#page > div.c-d.c-d-e > div.Zd-p-Sc > div:nth-child(1) > div.cc-dc-c > div > div.jc-c > table > tbody > tr')
for item in data:
    a = item.select("td.al > a")
    name = ''
    for x1 in a:
        name = x1.get_text()
    result = {
        'rank': item.select('td')[0].get_text(),
        'count': item.select('td')[2].get_text(),
        'name': name,
    }
    print(result)
