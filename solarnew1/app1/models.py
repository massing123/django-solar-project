from django.db import models


# Create your models here.
class signup(models.Model):
    First_Name=models.CharField(max_length=120)
    Last_Name=models.CharField(max_length=120)
    Company_Name=models.CharField(max_length=200)
    Company_Address=models.CharField(max_length=250)
    Communication_Address=models.CharField(max_length=250)
    Mobile_No=models.CharField(max_length=12)
    Landline_No=models.CharField(max_length=12)
    email=models.EmailField(max_length=60)
    GST=models.CharField(max_length=120)
    website=models.CharField(max_length=50)
    psw=models.CharField(max_length=20)
    psw_repeat=models.CharField(max_length=20) 
    date=models.DateField()
class contactme(models.Model):
    mname=models.CharField(max_length=50)
    memail=models.EmailField(max_length=120)
    mpassword=models.CharField(max_length=25)
    # mcheck=models.BooleanField(max_length=1)





