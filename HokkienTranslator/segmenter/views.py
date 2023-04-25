from django.shortcuts import render
def home(request):
    return render(request, "index.htm", {})

from read閩華對照含詞性 import read_kokgi2twblg
csvfile = open("../uni/閩華對照含詞性.tsv")
kokgi2twblg = read_kokgi2twblg(csvfile)

import jieba
from django.http import HttpResponse
def translate(request):
    Chinese = request.GET["Chinese"]
    words = list(jieba.cut(Chinese))
    translated_words = []
    for word in words:
        if word in kokgi2twblg:
            translated_word = kokgi2twblg[word]
            translated_words.append(translated_word)
        else:
            translated_words.append(word)
    return HttpResponse(" ".join(words) + "<br>"
                      + " ".join(translated_words))
