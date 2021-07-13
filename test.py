# print('Hello World!')
#
# weekdays = "Little Robert asked his mother for two cents.\
#      'What did you do with the money I gave you yesterday?'"
# print(weekdays)
#
# print("Who are you?")
# you = input()
# print("Hello!")
# print(you)

# import keyword
# print(keyword.kwlist)
import requests
url='https://s.weibo.com/top/summary/summary?cate=realtimehot'
strhtml=requests.get(url)
print(strhtml.text)