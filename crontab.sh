# 舆论场爬虫

*/20 * * * * /Users/yiwang/PycharmProjects/pythonProject/venv/bin/python /Users/yiwang/PycharmProjects/pythonProject/baidu.py >> ~/crontab/baidu.txt

*/20 * * * * curl https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all >> ~/crontab/bilibili.txt

*/10 * * * * /Users/yiwang/PycharmProjects/pythonProject/venv/bin/python /Users/yiwang/PycharmProjects/pythonProject/douyinTop.py >> ~/crontab/douyinTop.txt

*/5 * * * * /Users/yiwang/PycharmProjects/pythonProject/venv/bin/python /Users/yiwang/PycharmProjects/pythonProject/toutiao.py >> ~/crontab/toutiao.txt

*/5 * * * * /Users/yiwang/PycharmProjects/pythonProject/venv/bin/python /Users/yiwang/PycharmProjects/pythonProject/weiboHotSearch.py >> ~/crontab/weiboHotSearch.txt

*/5 * * * * /Users/yiwang/PycharmProjects/pythonProject/venv/bin/python /Users/yiwang/PycharmProjects/pythonProject/weiboHotTopic.py >> ~/crontab/weiboHotTopic.txt

*/5 * * * * /Users/yiwang/PycharmProjects/pythonProject/venv/bin/python /Users/yiwang/PycharmProjects/pythonProject/zhihu.py >> ~/crontab/zhihu.txt