 
import json
 
full_dic2 = {}

with open('full_dic.json') as json_file:
    full_dic = json.load(json_file)
 
alphabets = ['any', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 

for alphabet in alphabets:
    dic={}
    for key, value in full_dic.items():
        if key[0] == alphabet:
            dic[key] = value
    full_dic2[alphabet] = dic

full_dic2['any'] = full_dic

with open('full_dic2.json', 'w') as fp:
    json.dump(full_dic2, fp)
