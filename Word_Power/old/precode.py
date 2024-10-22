import numpy as np
import json


d = {}
with open("en.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = np.log(6281002 / int(val))

print(d['love'])


with open('dic.json', 'w') as fp:
    json.dump(d, fp)
