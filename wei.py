import json
from bs4 import BeautifulSoup
import requests
import re

url = 'https://d.weibo.com/231650'
headers = {
    'cookie': 'login_sid_t=3984b30b4771f2c27b2ce621049c4e7d; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=5111349392167.928.1622696586303; SINAGLOBAL=5111349392167.928.1622696586303; ULV=1622696586309:1:1:1:5111349392167.928.1622696586303:; SCF=AmznLzqIxPgc-Y87_riAeQkk2ZsjzDHp2HFgc5Mqo7IPFTahGHzSx5OXNq8vwWXj1Qdb35zT3O6U7X04vbzBbnU.; wb_view_log_3762099024=1920*10801%261792*11202; webim_unReadCount=%7B%22time%22%3A1626251844901%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A2%7D; SUB=_2AkMXsi18dcPxrABWnvoVxWLibolH-jykZ0SKAn7uJhMyAxh87goAqSVutBF-XI2EK9zse6cSTevFerxa14Msvpsb; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WFrhizeawmXsWk2_puxQxCi5JpVF02NSonEe027eK-0; UOR=,,login.sina.com.cn'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
# detail_url_html = re.search(r'\{(.*?)"domid"(.*?)\}', text)
# detail_url_html = re.search(r'\{(.*?)"domid"(.*?)\}', text)
