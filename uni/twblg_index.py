import csv

f2 = open("對應華語.csv")
(next(f2))
#print("n_no kokgi_v 閩南語詞目")
from collections import defaultdict
id_kokgi = defaultdict(list)
for kokgi_no,n_no,kokgi_v in csv.reader(f2):
#   print(n_no, kokgi_v, entry[n_no])
    id_kokgi[n_no].append(kokgi_v)
#for id, kokgi in id_kokgi.items():
 #   print(id, kokgi)


f1 = open("詞目總檔.csv")
(next(f1))

import json
entry = {}
#for 主編碼,屬性,詞目,音讀,文白屬性,部首 in csv.reader(f1):
 #   entry[主編碼] = 詞目
for j in json.load(open("dict-twblg.json")):
    heteronym = j['heteronyms'][0]
    definition = heteronym['definitions'][0]
    id = heteronym['id']
    if id in id_kokgi:
        if 'type' in definition:
            print(id, j['title'], id_kokgi[id][0], definition['type'], definition['def'], sep=',')
        else:
            print(id, j['title'], id_kokgi[id][0],             '無',   definition['def'], sep=',')
