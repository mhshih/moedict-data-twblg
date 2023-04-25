# 釋義含拼音即comma者後面不看
# 消失的3000千多筆...
import csv

def read_kokgi2twblg(csvfile):
    kokgi2twblg = {}
    for row in csv.reader(csvfile):
        # 釋義含拼音即comma者後面不看
        n_no, 閩南語詞目, kokgi_v, POS, 釋義 = row[:5]
#       if kokgi_v in kokgi2twblg:
#       print("\t".join(row))
        kokgi2twblg[kokgi_v] = 閩南語詞目
# 消失的3000千多筆...
    return kokgi2twblg

if __name__ == "__main__":
    csvfile = open("../uni/閩華對照含詞性.tsv")
    kokgi2twblg = read_kokgi2twblg(csvfile)
    for kokgi, twblg in kokgi2twblg.items():
        print(kokgi, twblg)
