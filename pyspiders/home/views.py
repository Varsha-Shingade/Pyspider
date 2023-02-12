from django.shortcuts import render,HttpResponse
from home.models import Freshers
from home.models import Experience

# Create your views here.
def index(request):
    #return HttpResponse('This is home page')
    return render(request,'index.html')
def pythond(request):
    return render(request,'pythond.html')
def pythonmt(request):
    return render(request,'pythonmt.html')
def pythonat(request):
    return render(request,'pythonat.html')
def sql(request):
    return render(request,'sql.html')
def web(request):
    return render(request,'web.html')
def contact(request):
    return render(request,'contact.html')
def placement(request):
    return render(request,'placement.html')
def apti(request):
    return render(request,'apti.html')
def verbal(request):
    return render(request,'verbal.html')
def fresher(request):
    if request.method=='POST':
        fname=request.POST.get('First_Name')
        lname=request.POST.get('Last_Name')
        dob=request.POST.get('dob')
        email=request.POST.get('Email_Id')
        pno=request.POST.get('Mobile_Number')
        address=request.POST.get('Address')
        city=request.POST.get('City')
        pin=request.POST.get('Pin_Code')
        state=request.POST.get('State')
        tyop=request.POST.get('ClassX_YrOfPassing')
        tp=request.POST.get('ClassX_Percentage')
        twop=request.POST.get('ClassXII_YrOfPassing')
        twp=request.POST.get('ClassXII_Percentage')
        diyop=request.POST.get('Diploma_YrOfPassing')
        dip=request.POST.get('Diploma_Percentage')
        dyop=request.POST.get('Graduation_YrOfPassing')
        dwp=request.POST.get('Graduation_Percentage')
        myop=request.POST.get('Masters_YrOfPassing')
        mp=request.POST.get('Masters_Percentage')
        courses=request.POST.get('Courses')
        fresher=Freshers(firstname=fname,lastname=lname,dob=dob,email=email,pno=pno,address=address,city=city,pincode=pin,state=state,tyop=tyop,tp=tp,twyop=twop,twp=twp,diyop=diyop,dip=dip,dyop=dyop,dwp=dwp,myop=myop,mp=mp,courses=courses)
        fresher.save()
        
    return render(request,'fresher.html')

def experience(request):
    if request.method=='POST':
        fname=request.POST.get('First_Name')
        lname=request.POST.get('Last_Name')
        dob=request.POST.get('dob')
        email=request.POST.get('Email_Id')
        pno=request.POST.get('Mobile_Number')
        address=request.POST.get('Address')
        city=request.POST.get('City')
        pin=request.POST.get('Pin_Code')
        state=request.POST.get('State')
        tyop=request.POST.get('ClassX_YrOfPassing')
        tp=request.POST.get('ClassX_Percentage')
        twop=request.POST.get('ClassXII_YrOfPassing')
        twp=request.POST.get('ClassXII_Percentage')
        dyop=request.POST.get('Graduation_YrOfPassing')
        dwp=request.POST.get('Graduation_Percentage')
        myop=request.POST.get('Masters_YrOfPassing')
        mp=request.POST.get('Masters_Percentage')
        courses=request.POST.get('Courses')
        dwp=request.POST.get('Graduation_Percentage')
        srno=request.POST.get('srno')
        companyname=request.POST.get('companyname')
        noofyears=request.POST.get('noofyears')
        designation=request.POST.get('designation')
        diyop=request.POST.get('Diploma_YrOfPassing')
        dip=request.POST.get('Diploma_Percentage')
        experience=Experience(firstname=fname,lastname=lname,dob=dob,email=email,pno=pno,address=address,city=city,pincode=pin,state=state,tyop=tyop,tp=tp,twyop=twop,twp=twp,dyop=dyop,dwp=dwp,myop=myop,mp=mp,courses=courses,srno=srno,companyname=companyname,noofyears=noofyears,designation=designation,iyop=diyop,dip=dip)
        experience.save()
        
    return render(request,'experience.html')



