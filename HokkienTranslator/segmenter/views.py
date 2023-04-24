from django.shortcuts import render
def home(request):
    return render(request, "index.htm", {})

from django.http import HttpResponse
def translate(request):
    Chinese = request.GET["Chinese"]
    return HttpResponse(Chinese)
