from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render




# User Register
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'Your Registration Complete', 'success')
            return redirect('account:login')
    else:
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'account/register.html', context)



# User-Log-in
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You're logged in successfully", 'success')
                return redirect('blog:home')
            
            else:
                messages.warning(request, "Wrong username or password", 'danger')
    
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form':form})
            



# User-Log-out
def user_logout(request):
    logout(request)
    messages.success(request, "logged out successfully", "success")
    return render(request, 'account/logout.html')