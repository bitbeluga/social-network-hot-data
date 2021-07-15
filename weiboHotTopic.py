import requests
import re
import time
import json
import pandas as pd
import xlsxwriter

global false, null, true
false = null = true = ''
top_name = []  # 话题名
top_reading = []  # 阅读数
top_rank = []  # 排名
top_subtitle = []  # 标题命
top_fans = []  # 话题参与人数
host_name = []  # 发起者名字
host_follow = []  # 发起者关注
host_fans = []  # 话题者粉丝
host_weibo = []  # 话题者微博数


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Cookie': 'UOR=www.xueshanlinghu.com,widget.weibo.com,www.xueshanlinghu.com; SUB=_2AkMpIlvAf8PxqwJRmPoRz2_lbY9yywvEieKffqobJRMxHRl-yT92qnU6tRB6AqJ1Ja0OS_Z4Sle1i9PePn9Y2j3r002F; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhMbmKIeS44Ywv2JBYP3dlp; login_sid_t=20e3745b135ada171ade3f91a392cf1f; cross_origin_proto=SSL; _s_tentry=passport.weibo.com; Apache=2694303126421.087.1585370372866; SINAGLOBAL=2694303126421.087.1585370372866; ULV=1585370372875:1:1:1:2694303126421.087.1585370372866:; YF-Page-G0=b1c63e15d8892cdaefd40245204f0e21|1585372515|1585372320'

    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response.encoding = 'UTF-8'
        return response.text
    return None


def analysis(topic):
    topicrank = re.search('<span class="(?:DSC_topicon_red|DSC_topicon|DSC_topicon_orange)">(.*?)</span>', topic, re.S)
    if topicrank is None:
        top_rank.append('')
    else:
        top_rank.append(topicrank.group(1))

    topicname = re.search('alt="(.*?)" class="pic">', topic, re.S)
    if topicname is None:
        top_name.append('')
    else:
        top_name.append(topicname.group(1))

    subtitle = re.search('class="subtitle">(.*?)</div>', topic, re.S)
    if subtitle is None:
        top_subtitle.append('')
    else:
        top_subtitle.append(subtitle.group(1))

    readingcount = re.search('<span class="number">(.*?) </span>', topic, re.S)
    if readingcount is None:
        top_reading.append('')
    else:
        top_reading.append(readingcount.group(1))

    ppname = re.search('class="tlink S_txt1"[\s]+>(.*?)</a></div>', topic, re.S)
    if ppname is None:
        host_name.append('')
        host_follow.append('')
        host_fans.append('')
        host_weibo.append('')

    else:

        host_name.append(ppname.group(1))
        aboutzcr = re.search(':<span><a target="_blank" href="[^0-9]+(.*?)\?', topic, re.S)

        if aboutzcr is not None:

            pp1 = "http://m.weibo.cn/api/container/getIndex?type=uid&value=" + str(aboutzcr.group(1))
            r = requests.get(pp1)
            if r.status_code == 200:
                html3 = r.text
                html4 = json.dumps(html3)
                content = json.loads(html4)
                jsoncontent = eval(content)
                userInfo = jsoncontent['data']['userInfo']
                statuses_count = userInfo['statuses_count']
                followers_count = userInfo['followers_count']
                follow_count = userInfo['follow_count']
                host_follow.append(follow_count)
                host_fans.append(followers_count)
                host_weibo.append(statuses_count)
        else:
            host_follow.append('')
            host_fans.append('')
            host_weibo.append('')

    return


def savetoexcel():
    print(len(top_name), len(top_rank), len(top_subtitle), len(top_reading), len(host_name), len(host_follow),
          len(host_fans), len(host_weibo))

    count = top_name.__len__()
    print(count)
    data = {'top_name': top_name[0:count], 'top_rank': top_rank[0:count], 'top_subtitle': top_subtitle[0:count],
            'top_reading': top_reading[0:count], 'host_name': host_name[0:count], 'host_follow': host_follow[0:count],
            'host_fan': host_fans[0:count], 'host_weibpo': host_weibo[0:count]}
    print(data)
    dfl = pd.DataFrame(data)

    writer = pd.ExcelWriter(r'C:\Users\yiwang\Desktop\sina.xlsx', engine='xlsxwriter',
                            options={'strings_to_urls': False})
    print(writer)
    dfl.to_excel(writer,
                 columns=['top_name', 'top_rank', 'top_subtitle', 'top_reading', 'host_name', 'host_follow', 'host_fan',
                          'host_weibpo'], index=False)
    writer.close()

    return


def main():
    for i in range(1, 10):
        print("Start...... page" + str(i))
        url = "https://d.weibo.com/231650?cfs=920&Pl_Discover_Pt6Rank__3_filter=&Pl_Discover_Pt6Rank__3_page=" + str(
            i) + "#Pl_Discover_Pt6Rank__3"
        html = get_one_page(url)
        handlepage = str(html).replace('\\t', "").replace('\\n', '').replace('\\', '').replace('#', '')
        topic = handlepage.split("pt_li S_line2")
        topic.pop(0)
        for each in topic:
            analysis(each)
        time.sleep(0.5)
        savetoexcel()


main()
