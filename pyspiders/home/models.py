from django.db import models

# Create your models here.
class Freshers(models.Model):
    firstname=models.CharField((""), max_length=50)
    lastname=models.CharField((""), max_length=50)
    dob=models.CharField((""), max_length=50)
    email=models.CharField((""), max_length=50)
    pno=models.CharField((""), max_length=50)
    address=models.CharField((""), max_length=50)
    city=models.CharField((""), max_length=50)
    pincode=models.CharField((""), max_length=50)
    state=models.CharField((""), max_length=50)
    tyop=models.CharField((""), max_length=50)
    tp=models.CharField((""), max_length=50)
    twyop=models.CharField((""), max_length=50)
    twp=models.CharField((""), max_length=50)
    diyop=models.CharField((""), max_length=50)
    dip=models.CharField((""), max_length=50)
    dyop=models.CharField((""), max_length=50)
    dwp=models.CharField((""), max_length=50)
    myop=models.CharField((""), max_length=50)
    mp=models.CharField((""), max_length=50)
    courses=models.CharField((""), max_length=50)

class Experience(models.Model):
    firstname=models.CharField((""), max_length=50)
    lastname=models.CharField((""), max_length=50)
    dob=models.CharField((""), max_length=50)
    email=models.CharField((""), max_length=50)
    pno=models.CharField((""), max_length=50)
    address=models.CharField((""), max_length=50)
    city=models.CharField((""), max_length=50)
    pincode=models.CharField((""), max_length=50)
    state=models.CharField((""), max_length=50)
    tyop=models.CharField((""), max_length=50)
    tp=models.CharField((""), max_length=50)
    twyop=models.CharField((""), max_length=50)
    twp=models.CharField((""), max_length=50)
    diyop=models.CharField((""), max_length=50)
    dip=models.CharField((""), max_length=50)
    dyop=models.CharField((""), max_length=50)
    dwp=models.CharField((""), max_length=50)
    myop=models.CharField((""), max_length=50)
    mp=models.CharField((""), max_length=50)
    courses=models.CharField((""), max_length=50)
    srno=models.CharField((""), max_length=50)
    companyname=models.CharField((""), max_length=50)
    noofyears=models.CharField((""), max_length=50)
    designation=models.CharField((""), max_length=50)
    
    
    





