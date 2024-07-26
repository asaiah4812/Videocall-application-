from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create_user(first_name, last_name, email, password1)
                user.save()
                login(request, user)
                messages.success(request, 'Your account has been successfully registered. PLease login to continue')
                return redirect('/')
            except:
                messages.warning(request, 'something went wrong. Please check form inputs')
                return render(request, 'videoconference_app/register.html')
        else:
            messages.error(request, "Passwords do not match")
            return render(request, 'videoconference_app/register.html')
    return render(request, 'videoconference_app/register.html')
                
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.info(request, 'Your accout has been successfully registered. PLease login to continue')
    #         return redirect('login')
    #     else:
    #         messages.warning(request, 'something went wrong. Please check form inputs')
    #         return redirect('register')
    # else:
    #     form = RegisterForm(request.POST)
    #     context = {'form': form}
    

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'login successfull, please enjoy you session')
            return redirect('/')
        else:
            messages.warning(request, 'something went wrong. please check form input')
            return redirect('login')
    else:
        return render(request, 'videoconference_app/login.html')
    


def logout_user(request):
    logout(request)
    return redirect('login')
def dashboard(request):
     return render(request, 'videoconference_app/dashboard.html')
 
def videocall(request):
    return render(request, 'videoconference_app/videocall.html', {'name' : request.user.username})
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'videoconference_app/join.html')