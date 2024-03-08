from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("notTwitter:index")
        
        else:
            fail_message = "Wrong username or password."
            messages.success(request, fail_message)
            return redirect("users:login")
        
    else:
        return render(request, 'registration/login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out')
    return redirect("notTwitter:index")


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration succesful!')
            return redirect("users:login")
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'registration/register_user.html', context)