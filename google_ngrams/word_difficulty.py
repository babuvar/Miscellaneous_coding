from wordStat import  NgramScraper
import sys
import json


s = NgramScraper()
result = s.query("love")

with open('web_dic.json') as json_file:
    web_dic = json.load(json_file)


diff_dic = {}


count = 0

for key, value in web_dic.items():
    count = count + 1
    result = s.query(key)
    diff_dic[key] = result
    print("%i words done"%count)


with open('/home/belle/varghese/DESY/words/diff_dic.json', 'w') as fp:
    json.dump(diff_dic, fp)


