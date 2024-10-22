# 15.653040079857101
import numpy as np
import json
import matplotlib.pyplot as plt
import math as mt

with open('web_dic.json') as json_file:
    web_dic = json.load(json_file)

with open('diff_dic.json') as json_file2:
    diff_dic = json.load(json_file2)

full_dic = {}

for key, value in web_dic.items():
    content = []
    if key not in  diff_dic:
        difficulty = 10
    else:
        difficulty = (diff_dic[key]*10)/15.653040079857101
        difficulty = mt.floor(difficulty)
    content.append(value)
    content.append(difficulty)
    full_dic[key] = content
 

with open('full_dic.json', 'w') as fp:
    json.dump(full_dic, fp)


#plt.hist(diff, bins=100)
#plt.show()

