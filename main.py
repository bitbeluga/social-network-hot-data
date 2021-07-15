# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests as requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/billboard'
headers1 = {
    'authority': 'www.zhihu.com', 'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"', 'sec-ch-ua-mobile': ' ?0',
    'upgrade-insecure-requests': ' 1',
    'user-agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': ' none',
    'sec-fetch-mode': ' navigate',
    'sec-fetch-user': ' ?1',
    'sec-fetch-dest': ' document',
    'accept-language': ' en,zh;q=0.9,de;q=0.8,zh-CN;q=0.7',
    'cookie': '_xsrf=OlwuSq0LcOlsocN0VojLfmkREzUKPK3I; _zap=714ebbf2-b82b-4a6b-acf6-c380f603be70; d_c0="ADDd704yLxOPTuVyIMMTg6JtUXSdGAkEcLU=|1622364819"; __snaker__id=Jpn8BgKCSLybNge4; gdxidpyhxdE=Mmfv9fPS9t19rM%2BLZuwMq%2FamxzMOj2YrUuU5ixHWn0Vwc51YWfUNYxeI6zyjaG27cxh2vTD%2FXJ%2FnKjjGsmRtfP37VK1k098g2lzCtiTC05XQlp%2FO%2BRK%2BZB0%5CEQPkfyV8p1DY3mBA%2FzGqkeVChIKkW%2B4hSqZG8AzphdIoeWjJIC2DVYZw%3A1622365720796; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=OIIp0QANnvsR%2Fn3xLAz5%2FqO%2BBsYXeRPOnyDk7y20p2YcCg9nEd6vTzONEK1z%2B93T88GP7B4XywjtxTpJjC%2FLaYebac4hsoIzbYRLg5P3B2rAU80q83lLwqLQwrH2QHjubnM%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee86ee72ad868fa5f321f8b08bb7d14f829f8eabaa74f8f5a8b1f36281bba4d0d02af0fea7c3b92a8d978791b35b8392a297f25aedb2fd99cf4bbaebe192ce2182ad97b9e85a9491a29ac761f5a7fed1f33a9bbd8d88bc6687bcfa97d7728d928bacb472e9e7fdb5bb348590f9a3b754bba9a695fb60b496a6a4ae48a387ab83e469f8b8bd90cc72a2879eade63f94ed8ed3f14b97e80092bb39b094b992cf5bb5ae88d3d444aaabae8fd037e2a3; YD00517437729195%3AWM_TID=A3u9Kv3vvehFBBAQRQc6kor1OomHe0qZ; l_n_c=1; n_c=1; z_c0=Mi4xcm5nM0FnQUFBQUFBTU4zdlRqSXZFeGNBQUFCaEFsVk5vS0NnWVFDcVFOdkdZTmt4dXdhdk5TLXZBYmc2VzNaekJB|1622364832|a088f172770ce7885e82bf85b721b572601a69a6; q_c1=404e33b7a78e426f977a4cb2866f295d|1624106846000|1624106846000; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1626245447,1626245584,1626248544,1626253185; SESSIONID=ucyJx8EjnDguMkBoq4SkJCLLQ7EydYdHj7Mj8NJIilN; JOID=UlAXBk1v5rL6x9tuA2o4ramM7E8SEo_Ms7nrIW4Hqt-IibYkZrtWWJ_J2WMHRKegSsch40jJBzNkkeQ_ED2sbqA=; osd=Vl8SCkpr6bf2wN9hBmY_qaaJ4EgWHYrAtL3kJGIArtCNhbEgab5aX5vG3G8AQKilRsAl7E3FADdrlOg4FDKpYqc=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1626259735; KLBRSID=ca494ee5d16b14b649673c122ff27291|1626259735|1626258901',
}
print(headers1)

response = requests.get(url, headers=headers1)
print(response)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
