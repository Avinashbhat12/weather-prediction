from contextlib import redirect_stderr
import email
from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from .models import Register

import pandas as pd
from .models import weatherdata

from sklearn.naive_bayes import GaussianNB


# Create your views here.
def home(request):
    return render(request,"home.html")
"""
def register(request):
    if request.method=="POST":
      usrname=request.POST['username']
      pswd=request.POST['pwd']
      mail=request.POST['email']
      conf=request.POST['cpwd']
      if pswd==conf:
            if RegisterData.objects.filter(username=usrname).exists():
                messages.info(request,"username exists")
                return render(request,"register.html")
            elif RegisterData.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                return render(request,"register.html")
            else:
            
                user=RegisterData.objects.create(username=usrname,password=pswd,email=mail)
                user.save()
                return render(request,"login.html")
      else:
            messages.info(request,"password not matching")
            return render(request,"register.html")  
    else:
            return render(request,"register.html")  """ 



def register(request):
    if request.POST.get('email'):

      usrname=request.POST['username']
      pswd=request.POST['pwd']
      mail1=request.POST['email']
      conf=request.POST['cpwd']
      if pswd==conf:
            if Register.objects.filter(username=usrname).exists():
                messages.info(request,"username exists")
                return render(request,"register.html")
            elif Register.objects.filter(email= mail1).exists():
                messages.info(request,"email exists")
                return render(request,"register.html")
            else:
                # user=User.objects.create_user(username=usrname,password=pswd,email=mail)    

                user=Register.objects.create(username=usrname,password=pswd,email=mail1)
                user.save()
                return render(request,"home.html")
      else:
            messages.info(request,"password not matching")
            return render(request,"register.html")
    else:
        return render(request,"register.html")
"""
def login(request):
    if request.method == 'POST':
        user=request.POST['username']
        passw=request.POST['pwd']

        user=auth.authenticate(username=user,pwd=passw)

        if user is not None:
            auth.login(request,user)
            return  render(request,'home.html')
        else:
            messages.info(request,'invalid credential')
            return render(request,'login.html') 
    else:
        return render(request,'login.html') """


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        print("email is", username)
        print("pass is", password)
        d = Register()
        userdetails = d.validteuser(username=username,password=password)
        #print(userdetails.Email)
        print(userdetails)
        if userdetails =='yes':
            print('Successfull Login')
            messages.info(request,"successfully login")
            return redirect('predictinput')
        else:
            print('Failure Login')
            messages.info(request,"failure login")
            return render(request, 'login.html')
    else:
        return render(request,"login.html")

"""def login(request):
   if request.method=='POST':
        user =request.POST['username']
        passw=request.POST['pwd']
        if Register.objects.filter(username=user,password=passw).exists():
            if Register.objects.filter().exists():
                return render(request,'predictinput.html')
            else:
                messages.info(request,"Wrong Password")
                return render(request,'login.html')
        else:
            messages.info(request,"Invalid Username")
            return render(request,'login.html')
   else:

        return render(request,'login.html')
"""
def  predictinput(request):
    if request.method=="POST":
        tmx=int(request.POST['temp_max'])
        tmn =int(request.POST['temp_min'])
        prc=int(request.POST['precipitation'])
        wn=int(request.POST['wind'])
        if tmx > tmn:
         df = pd.read_csv(r"static/dataset/weather.csv")
         df.dropna(inplace=True)
         df.isnull().sum()
         X=df[["precipitation","temp_max","temp_min","wind"]]
         Y=df[["weather"]]
        #X_train = df[['tmx','tmn','prc','wn']]
        #y_train = df[['weatherp']]
         from sklearn.naive_bayes import GaussianNB
         ran = GaussianNB()
         ran.fit(X,Y)
         prediction = ran.predict([[tmx,tmn,prc,wn]])
         print(prediction)
         weatherp=weatherdata.objects.create(temp_max=tmx,temp_min=tmn,precipitation=prc,wind=wn)
         weatherp.save()
         return render(request,'predictout.html',
                      {"weather": prediction,'temp_max':tmx,'temp_min':tmn,'precipitation':prc,"wind":wn})
        else:
             return render(request, 'predictinput.html')
                   
    else:
        return render(request, 'predictinput.html')

def predictout(request):
    
    tmx=request.POST['temp_max']
    tmn =request.POST['temp_min']
    prc=request.POST['precipitation']
    wn=request.POST['wind']

    df = pd.read_csv(r"static/dataset/weather.csv")
    df.dropna(inplace=True)
    df.isnull().sum()
    X=df[["precipitation","temp_max","temp_min","wind"]]
    Y=df[["weather"]]
        #X_train = df[['tmx','tmn','prc','wn']]
        #y_train = df[['weatherp']]
    from sklearn.naive_bayes import GaussianNB
    ran = GaussianNB()
    ran.fit(X,Y)
    prediction = ran.predict([[tmx,tmn,prc,wn]])
    print(prediction)
    weatherp=weatherdata.objects.create(temp_max=tmx,temp_min=tmn,precipitation=prc,wind=wn)
    weatherp.save()
    return render(request,'predictout.html',
                      {"weather": prediction,'temp_max':tmx,'temp_min':tmn,'precipitation':prc,"wind":wn})
    