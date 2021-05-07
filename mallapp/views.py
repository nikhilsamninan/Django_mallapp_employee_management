from django.shortcuts import render,HttpResponse,redirect
from malldatabase import settings
from .models import Employee,Images
from .form import Employeeform,Imgform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url='/userlogin')
def home(request):
    if request.session.get('usertype')=="admin":
        details = Employee.objects.all()
        return render(request,'index.html',{'data':details})
    elif request.session.get('usertype')=="normal user":
        return redirect(userhome)
    
@login_required(login_url='/userlogin')
def userhome(request):
    details = Employee.objects.all()
    image = Images.objects.get(user=request.user.id)
    print(image)
    return render(request,'userhome.html',{'data':details,'images':image})


def modelform(request):
    if request.method == "POST":
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            context = {'myform':form}
            return render(request,'modelform.html',context)
    else:
        form = Employeeform()
        context = {'myform':form}
        return render(request,'modelform.html',context)


def registrationfn(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print("form post")
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            send_mail('Greeetings from Nikhil Sample Works','You successfully registerd with Mall Employee App now you can login',settings.EMAIL_HOST_USER,[user])
            return redirect(home)
    form = UserCreationForm()
    return render(request,"userreg.html",{'myform':form})


def loginfn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (username)
        print (password)
        check = authenticate(request,username = username,password = password)
        print (check)
        if check:
            login(request,check)
            if username == "admin@admin.com" and password == "root@123":
                request.session['usertype'] = "admin"
                request.session['username'] = username
                return redirect(home)
            else:
                request.session['usertype'] = "normal user"
                request.session['username'] = username
                return redirect(userhome)
    return render(request,"login.html")

def logoutfn(request):
    logout(request)
    return redirect(home)


def update(request,id):
    emp_update = Employee.objects.get(id=id)
    if request.method=="POST":
        form = Employeeform(request.POST,instance =emp_update)
        if form.is_valid():
            age = form.cleaned_data['age']
            if age>5:
                form.save()
                return redirect(home)
            else:
                return render(request,"modelform.html",{'myform':form})
        else:
            return render(request,"modelform.html",{"myform":form})    
    form=Employeeform(instance=emp_update)
    return render(request,"modelform.html",{"myform":form})

def delete(request,id):
    p = Employee.objects.get(id=id)
    p.delete()
    return redirect(home)

def uploading(request):
    if request.method == 'POST':
        form = Imgform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(userhome)
    
    form = Imgform()
    return render(request,'uploadform.html',{'form':form})


    
# send_mail('subject','message',settings.Email_HOST_USER,['shinyannninan@gmail.com'])