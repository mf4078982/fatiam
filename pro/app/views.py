from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import My_model
from .forms import My_f
from django.contrib.auth import logout
# Create your views here.
def login(request):
    if request.method == 'POST':
        f = AuthenticationForm(request, request.POST)
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        if f.is_valid():
            user = AuthenticationForm(username=uname,password=pass1)    
            if user is not None:
                login(request,user)
        return redirect('add')
                
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            return HttpResponse('pass1 and pass2 not equal')

        
            
        else:
            user = User.objects.create_user(username=uname,email=email,password=pass1)
            user.save()
            return redirect('login')
        
    return render(request,'register.html')
def add(request):
    s = My_model.objects.all()
    if request.method == 'POST':
        sm = My_f(request.POST)
        if sm.is_valid():
            sm.save()
            sm = My_f()
    else:
        sm = My_f()
       
    return render(request,'add.html',{'forms':sm,'nice':s})
def delete(request,id):
    m = My_model.objects.get(pk=id)   
    if request.method == 'POST':
        m.delete()
        
    return redirect('add')
def update(request,id):
    m = My_model.objects.get(pk=id)
    if request.method == 'POST':
        sm = My_f(request.POST , instance=m) 
        if sm.is_valid():
            sm.save()
            sm = My_f()
    else:
        sm = My_f(instance=m)
        sm = My_f()
    return render(request,'update.html',{'forms':sm})
def logout(request):
    logout(request)
    return redirect('add')
    