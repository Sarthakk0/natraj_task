from django.shortcuts import render,HttpResponse
import pymysql as sql
from django.views import View


def connection():
    try:
        db = sql.connect(host = "localhost", port = 3306 , password = "",user  = "root" , database  = "task1")
    except: 
        db = None
        cursor = None
    else:
        cursor = db.cursor()
    return cursor,db

def home(request):
    return render(request,"home.html")

def vehiclelist(request):
    return render(request,"vehicle.html")

def addv(request):
    return render(request,"addv.html")
#render(request,"addv.html",{'msg':"Vehicle sucessfully added"})
#render(request,"addv.html",{ 'msg':"Vehicle details updated"})
class afterform(View):
    def get(self,request):
        return render(request,"addv.html")

    def post(self,request):
        name  = request.POST.get('vname')
        model = request.POST.get('model')
        engine = request.POST.get('engine')
        price = request.POST.get('price')
        print(name)
        cursor,db = connection()
        if db:
            cmd = f"select * from vehicle where name = '{name}';"
            cursor.execute(cmd)
            data  = cursor.fetchone()
            if data :
                cmd2 = f"update vehicle set name = {name},model = {model} , engine = {engine},price = {price} where name  = {name};"
                cursor.execute(cmd2)
                return render(request,"addv.html",{'msg':"Vehicle sucessfully added"})
            else:
                cmd3 = "insert into vehicle values('{engine}','{model}','{engine}', '{price}' );"
                cursor.execute(cmd3)
                return render(request,"addv.html",{ 'msg':"Vehicle details updated"})
        else:
            return HttpResponse("<p>No Database </p>")
