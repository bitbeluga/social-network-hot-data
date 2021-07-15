import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/billboard'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
