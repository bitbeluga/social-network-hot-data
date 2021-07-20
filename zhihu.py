# from bs4 import BeautifulSoup
# import requests

#
# url = 'https://www.zhihu.com/billboard'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "lxml")
# print(soup)
#
# data = soup.select(
#     '#root > div > main > div > a')

# for item in data:
# result = {
#     'rank': item.select('div.HotList-itemPre > .HotList-itemIndex')[0].get_text(),
#     'count': item.select('div.HotList-itemBody > .HotList-itemMetrics')[0].get_text(),
#     'title': item.select('div.HotList-itemBody > .HotList-itemTitle')[0].get_text(),
# }
# print(result)


import re
import requests
import pandas as pd
from datetime import datetime

print("\n""\n""Zhihu start_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
Domain_Name = 'https:'
headers = {
    'Referer': "https://www.zhihu.com/billboard",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

url = 'https://www.zhihu.com/billboard'

response = requests.get(url, headers=headers)

html = response.text
# print('----------------???----------------')
# ???????????
content = re.findall(r'<div class="HotList-itemTitle">([\s\S]+?)</div>', html, re.M)  # ??????
hot = re.findall(r'<div class="HotList-itemMetrics">([\s\S]+?)</div>', html, re.M)  # ??????
url = re.findall(r'"link":{"url":"([\s\S]+?)"}},', html, re.M)  # ???????
describe = re.findall(r'"excerptArea":{"text":"([\s\S]+?)"},', html, re.M)  # ???????
dts = []
rank = 0
for i in range(len(content)):
    rank = rank + 1
    lst = [content[i], rank, hot[i], str(url[i]).replace('u002F', '')]
    dts.append(lst)
df = pd.DataFrame(dts, columns=['name', 'rank', 'hot', 'url'])
df.to_excel('./zhihu' + str(datetime.now().strftime('%Y%m%d')) + '.xlsx',
            encoding='gbk')  # ??excel?
print('????')

print("Zhihu end_at:", datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
