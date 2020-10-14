from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
import time
from .gallery import gallery
from .models import Callback,Visitor,Ip,Mopup,Round1,Round2,College_predictor
import datetime
from django.db.models import Q
import sqlite3
import csv


def home1(request):
    d={}
    if request.method == "POST":
        callback = Callback()
        callback.name=request.POST["firstname"]
        # callback.lastname=request.POST["lastname"]
        callback.phone=request.POST["phone"]
        # callback.email = request.POST["email"]
        d.update(request.POST)
        if len(d["phone"][0]) > 0 and len(d["firstname"][0]) > 0:
            callback.time = datetime.datetime.now()
            print(callback.time)
            callback.save()            
            return HttpResponseRedirect("/registration")
    return render(request, "home/home.html") 
    
def registration(request):
    return render(request, "home/registration.html")

def ivano(request):
    return render(request, 'home/ivano.html')
    
def view_gallery(request):
    return render(request, 'home/gallery.html', gallery)
        
def poltava(request):
    return render(request, 'home/poltava.html')

def lviv(request):
    return render(request, 'home/lviv.html')

def bogo(request):
    return render(request, 'home/bogo.html')

# def rep(college):
#     for i in range(len(college)):
#         if not college[i]:
#             college[i] = None
#     return college

def predictor(request):
    if request.method == "POST":
        try:
            user = College_predictor()
            assert(request.POST["name"])
            user.name=request.POST["name"]
            user.number=request.POST["number"]
            user.email=request.POST["email"]
            user.save()
            args = {"colleges":None,"user":1}
            response = render(request, 'home/predictor.html', args) 
            print("not cookie")
            response.set_cookie("user", value="1", max_age=200000)
            print("cookie")
        except Exception:
            pass   
            # args = {"colleges": None, "user": request.COOKIES["user"]}
            # response = render(request, 'home/predictor.html', args) 
        # print(request.POST["number"])
        # print(request.POST["email"])
        try:
            a=request.POST["round"]
        except Exception:
            a=1
        if a == "Round-1":            
            colleges = Round1.objects.all().filter(state=request.POST["state"],course=request.POST["course"],)
            args = {"colleges": colleges,"sample":"round-1"}
            response = render(request, 'home/predictor.html', args) 
            
        elif a == "Round-2":            
            colleges = Round2.objects.all().filter(state=request.POST["state"],course=request.POST["course"],)
            args = {"colleges": colleges,"sample":"round-2"}
            response = render(request, 'home/predictor.html', args) 
            
        elif a == "Mop up":            
            colleges = Mopup.objects.all().filter(state=request.POST["state"],course=request.POST["course"],)
            args = {"colleges": colleges, "sample": "mopup"}          
            response = render(request, 'home/predictor.html', args) 
        else:
            pass
        return response

    try:
        assert (request.COOKIES["user"])
        args = {"colleges": None, "user": request.COOKIES["user"]}
        response = render(request, 'home/predictor.html', args) 
    except Exception:
        # pass
        args = {"colleges": None, "user": None}
        response = render(request, 'home/predictor.html', args)
      
    return response
    
def college_predictor(request):

    course = request.POST['course']
    rank = request.POST["rank"]
    caste = request.POST['cast']
    pwd = request.POST['pwd']
    # round1_filter = Round1.objects.all().filter(course=course)
    # round2_filter = Round2.objects.all().filter(course=course)
    # mopup_filter = Mopup.objects.all().filter(course=course,ew_cr>)
    # print(type(caste))
    try:
        if caste == "pw":
            # print(type(request.POST["caste"]),"----------")
            round2_filter = Round2.objects.filter(course=course,pw_cr__gte=rank)
            # print(round2_filter,"..............")
            args = {"colleges": round2_filter}
            # print(round2_filter,"===============")
            response = render(request, 'home/predictor.html', args)
    except Exception as e:
        print(e)
        # print(e,"///////")
        args = {"colleges": 12}
        # print(round2_filter,"===============")
        response = render(request, 'home/predictor.html', args)
            
    return response



# def data(request):
    
#     with open('round2.csv', "r") as f:
#         csv_reader = csv.reader(f)
#         # college = list(map())
#         n=0
#         for college in csv_reader:
#             n += 1
#             # if n < 111:
#             #     continue
#             # print(len(college))
#             # print(college)
#             college = rep(college)
#             coll = Round2()
#             coll.fill(college)
#             coll.save()
#             print(n)
#             # if n==20:
#             #     break
#     return render(request,"1.html")