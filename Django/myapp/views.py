from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import pymysql
from myapp.form import *

# Create your views here.
#def sayhello(request):
#    return HttpResponse("hello")

def index(request):
    return HttpResponse("index")    
    
def member(request):

#    return render(request,"member.html",locals())
    return render(request,"member.html",locals())

def sayhello2(request,username):
    return HttpResponse("hello  "+username)
    
def memberCreate(request):
    if request.method == "POST":
        uid=int(request.POST['id'])
        name=request.POST['name']
        tel=request.POST['tel']
        addr=request.POST['addr']
        db=pymysql.connect(host="127.0.0.1",user="admin",password="admin",db="mdu",charset="utf8")
        cursor=db.cursor()
        sql="insert into member (id,name,tel,addr) values ({0}, '{1}', '{2}', '{3}')".format(uid,name,tel,addr)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
       # pass #檢查並寫入資料庫
        return redirect("/member/")
    else:
        post=memberform()
        return render(request,"memberCreate.html",locals())

    
def test (request,score):  
    # score=int(score)
    a=[{'name':'makoto','age':'24'},{'name':'oroku','age':'18'}]
    b=[]
    c=range(15)
    return render(request,"test.html",locals())
 
def memberList(request):
    db=pymysql.connect(host="127.0.0.1",user="admin",password="admin",db="mdu",charset="utf8")
    cursor=db.cursor()
    sql="select * from member"
    cursor.execute(sql)
    data=cursor.fetchall()
    nums=len(data)
    db.commit()
    cursor.close()
    db.close()
    return render(request,"memberList.html",{'data':data})
    
def memberListone(request):
    if request.method == "POST":
        db=pymysql.connect(host="127.0.0.1",user="admin",password="admin",db="mdu",charset="utf8")
        cursor=db.cursor()
        word=request.POST['word']
    
        if request.POST['searchselect'] == 'name':
               sql="select * from member where name = '{0}'".format(word)
            
        elif request.POST['searchselect'] == 'tel':
                sql="select * from member where tel = '{0}'".format(word)
            
        elif request.POST['searchselect'] == 'addr':
                sql="select * from member where addr = '{0}'".format(word)
                
        cursor.execute(sql)
        data=cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        return render(request,"test2.html",{'data':data}) 
    
    else:
        return render(request,"memberListone.html")
        
def memberDelete(request,uid):
    db=pymysql.connect(host="127.0.0.1",user="admin",password="admin",db="mdu",charset="utf8")
    cursor=db.cursor()
    sql="delete from member where id={0}".format(uid)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return redirect("/member/")


def memberUpdate(request,uid):
    if request.method == "POST":
       # uid=int(request.POST['id'])
       name=request.POST['name']
       tel=request.POST['tel']
       addr=request.POST['addr']
       db=pymysql.connect(host="127.0.0.1",user="admin",password="admin",db="mdu",charset="utf8")
       cursor=db.cursor()
       sql="update member set name='{1}',tel='{2}',addr='{3}',id='{0}' where id = {0}".format(uid,name,tel,addr)
       cursor.execute(sql)
       db.commit()
       cursor.close()
       db.close()
        
       
       return redirect("/memberList/") 
    else:
        db=pymysql.connect(host="127.0.0.1",user="admin",password="admin",db="mdu",charset="utf8")
        cursor=db.cursor()
        sql="select * from member where id={0}".format(uid)
        cursor.execute(sql)
        db.commit()
        data=cursor.fetchone()
        cursor.close()
        db.close()
        return render(request,"memberUpdate.html",{"data":data})

def memberForm(request):
    postform = memberform()
    return render(request, "test3.html", locals())
    
    
    
    
    
    
    
    
    
    