from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from iotapp.models import CustomUser
# Create your views here.
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            if not user.is_superuser:
                auth.login(request,user)
                print("user authenticate")
                return redirect("dashboard")
            
            else:
                auth.login(request,user)
                print("super user authenticate")
                return redirect("/admin")
        else:
            messages.info(request,"invalid credentials",'login.html')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        token=request.POST.get("token")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if not all([first_name, last_name, token, username, email, password, confirm_password]):
            messages.info(request, "Please fill all the fields", 'register.html')
            return redirect('register')
        if password==confirm_password:
            if len(password)<8:
                messages.info(request,"Password must be 8 or more character long",'register.html')
                return redirect('register')
            print(len(token))
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,"Username is taken",'register.html')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,"email taken",'register.html')
                return redirect('register')
            else:
                user=CustomUser.objects.create_user(username=username,token=token,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,"password not matching",'register.html')
        return redirect('dashboard') #once registration done go home page
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('login')