from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from HotelApp.models import Employee,Upload
from HotelApp.forms import EmployeeForm,SignupForm,UploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def hotel(request):
    dt=datetime.now()
    mydict={"date":dt,"name":"Nitin","email":"ngour@edsystango.com"}
    #return HttpResponse("<h1>Welcome at HotelApp Date:"+str(dt)+" </h1>")
    return render(request,"HotelApp/index.html",context=mydict)

@login_required
def home(request):
    #fetch record from Table  select * from Employee
    emplist=Employee.objects.all()
    mydict={'emplist':emplist}
    print(emplist)
    return render(request,"HotelApp/home.html",context=mydict)

@login_required
def emp(request):
    empform=EmployeeForm()
    mydict={'empform':empform}
    if request.method=='POST':
        empform=EmployeeForm(request.POST)
        empform.save()# insert query
        mydict['msg']='Data Inserted'
    return render(request,"HotelApp/employee.html",context=mydict)

def signup(request):
    sform=SignupForm()
    mydict={'sform':sform}
    if request.method=='POST':
        sform=SignupForm(request.POST)
        user=sform.save() #a a  a admin
        print(user.password,user.first_name)
        user.set_password(user.password)
        user.save()
        mydict['msg']='User Registered Successfylly...'
    return render(request,"HotelApp/signup.html",context=mydict)

@login_required
def upload(request):
    uform=UploadForm()
    mydict={'uform':uform}
    if request.method=='POST':
        uform=UploadForm(request.POST,request.FILES)
        if uform.is_valid():
            data=uform.save(commit=False)
            data.author=request.user
            data.save()
            mydict['msg']='File uploaded Successfylly...'
    images=Upload.objects.all().order_by('-uploaddate')
    mydict['images']=images
    return render(request,"HotelApp/uploadimage.html",context=mydict)

def deleteEmp(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    emplist=Employee.objects.all()
    mydict={'emplist':emplist,'msg':'Data Deleted'}
    return render(request,"HotelApp/home.html",context=mydict)
