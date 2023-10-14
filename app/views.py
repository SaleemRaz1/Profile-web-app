from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . forms import CreateUserForm,ProfileForm
from django.contrib.auth.decorators import login_required
 
# Create your views here.

@login_required(login_url='login')
def Home(request):
    return render(request,'home.html')



@login_required(login_url='login')

def Profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            username=request.user.username
            messages.success(request,f'{username} , your profile is updated')
            return redirect('/')
        
    else:
        form=ProfileForm(instance=request.user.profile)
        context={
            'form':form
        }
        
        
        return render(request,'profile.html',context)
    
 
 
 

def Login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        
        if user is not None:
            login(request,user)
            messages.info(request,f'{uname}, You are logged in ')
            return redirect('home') 
        else:
            messages.info(request,'Invalid username or passowrd' )
            return redirect('login')
    return render(request,'login_page.html')




def Register(request):
   form=CreateUserForm()
   if request.method=='POST':
       form=CreateUserForm(request.POST)
       if form.is_valid():
           form.save()
           messages.info(request,'Account is Created')
           redirect('login')
           
       else:
           context={'form':form}
           messages.info(request,'Invalid Credentials')
           return render(request,'register_page.html',context)
               
   context={'form':form}    
   return render(request,'register_page.html',context)


@login_required(login_url='login')

def Logout(request):
    return render(request,'logout.html')
