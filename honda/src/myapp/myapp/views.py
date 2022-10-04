from django.http import HttpResponse
from django.shortcuts import render

def Home_page(request):
    #mycontent="This is my home page"
    return render(request,'hello.html')     #{"content":mycontent})