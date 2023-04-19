import csv

f1 = open("詞目總檔.csv")
print(next(f1))

entry = {}
for 主編碼,屬性,詞目,音讀,文白屬性,部首 in csv.reader(f1):
    entry[主編碼] = 詞目


f2 = open("對應華語.csv")
print(next(f2))

for kokgi_no,n_no,kokgi_v in csv.reader(f2):
#   if n_no not in entry:
    print(n_no, kokgi_v, entry[n_no])
