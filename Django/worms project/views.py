from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import pymysql
from django.urls import reverse
from bugapp.form import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def newsFind(request):
    if request.method == "POST":
        if request.POST['url'] == "udn":
            url="https://udn.com/search/word/2/"+request.POST['keyword']
        elif request.url == "new":
            pass
        else:
            pass
          
        doc1=requests.get(url)
        if doc1.status_code==200:
            soup=BeautifulSoup(doc1.text.encode('utf-8'),"lxml") 
        else:
            print("bs failed")

        titles=soup.select("div.story-list__news div.story-list__text h2 a")
        times=soup.select("div.story-list__text  div.story-list__info  time ")

        titlelist=[]
        timelist=[]
        contentlist=[]
        linklist=[]


        for i in range(len(titles)):
            art=requests.get(titles[i].get('href'))
            artsoup=BeautifulSoup(art.text.encode('utf-8'),"lxml")
            content=""
            contentsoup=artsoup.select("article.article-content div.article-content__paragraph section.article-content__editor p")
            for j in range(len(contentsoup)):
                content += contentsoup[j].getText()
            dates=datetime.strptime(times[i].string[:10], '%Y-%m-%d').date()
            titlelist.append(titles[i].string)
            linklist.append(titles[i].get('href'))
            timelist.append((times[i].string[:10]))
            contentlist.append(content)
        
        newslist=[]
        for i in range(len(titlelist)):
           newslist.append([titlelist[i],linklist[i],timelist[i],contentlist[i]])
        return render(request,"newsList.html",locals())
    
    else:
        postform=postform1()
        return render(request,"newsFind.html",locals())