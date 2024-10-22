# 15.653040079857101
import numpy as np
import json
import matplotlib.pyplot as plt
import math as mt

with open('full_dic.json') as json_file:
    full_dic = json.load(json_file)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for key, value in full_dic.items():
    if key[0] == 'q':
        print(key, value[1]) 

 



