# 僅有台羅拼音翻譯的台華共同詞只取第一個音
import csv
zh2min = {}
for line in open("../uni/華語對照閩南語表.tsv"):
    # 僅有台羅拼音翻譯的台華共同詞只取第一個音
    n_no, kokgi_v, 閩南語詞目 = line.split()[:3]
    zh2min[kokgi_v] = 閩南語詞目
    print(kokgi_v)

