from django.contrib.messages.api import info
from django.http import request
from app1.models import contactme,signup
from django.shortcuts import redirect, render
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
def contactus(request):
    return render(request,"contactus.html")
def material_inspection(request):
    return render(request,"material_inspection.html")
def plant_testing(request):
    return render(request,"plant_testing.html") 
def manpower_equi(request):
    return render(request,"manpower_equi.html") 
def Project_Registration(request):    
    return render(request,"Project_Registration.html")
def contactus(request):
    # return render(request,"contactus.html")
     if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = authenticate (username=email,password=password)
        print(user)
        z=contactme(mname=email,memail=email,mpassword=password)
        z.save()
        if user is not None:
                    login(request,user)
                    return redirect("/")
        else:
                    messages.info(request,'Invalid Credentials')
                    return redirect('contactus')

     else:
        return render(request,"contactus.html")


  
        


    
def signupme(request):
    if request.method == "POST":
        
        First_Name= request.POST.get('First_Name')              
        Last_Name=request.POST.get('Last_Name')
        Company_Name=request.POST.get('Company_Name')
        Company_Address=request.POST.get('Company_Address')
        Communication_Address=request.POST.get('Communication_Address')
        Mobile_No=request.POST.get('Mobile_No')
        Landline_No=request.POST.get('Landline_No')
        email=request.POST.get('email')
        GST=request.POST.get('GST')
        website=request.POST.get('website')
        psw=request.POST.get('psw')
        psw_repeat=request.POST.get('psw_repeat')
        user=User.objects.create_user(username=email,password=psw,email=email,first_name=First_Name,last_name=Last_Name)
        user.save();
            
        y=signup(First_Name=First_Name,Last_Name=Last_Name,Company_Name=Company_Name, Company_Address= Company_Address,Communication_Address=Communication_Address,Mobile_No=Mobile_No,Landline_No=Landline_No,email=email,GST=GST,website=website,psw=psw,psw_repeat=psw_repeat,date=datetime.today())
        y.save()
        

                #send email
        receipt_mail=[y.email,]
        send_mail(
                        'Welcome to PVSolarClick',
                        'Hi  thank you for registering in PVSolarClick.',
                        'pvsolarclick@gmail.com',
                        receipt_mail,
                        fail_silently=False,
                        )
        print("usercreated")
        return redirect('contactus')
        messages.success(request,"Sign Up Success")
        
    else:
        return render(request,"signupme.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
