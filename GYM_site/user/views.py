from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.messages.api import success
from .forms import registerForm, loginForm, UserUpdateForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def registerUser(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        if User.objects.filter(username=username):
            messages.warning(request,"Bu istifadəçi adı artıq mövcuddur")
            return redirect('register')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        if User.objects.filter(email=email):
            messages.warning(request,"Bu email adresi qeydiyyatdan keçmişdir")
            return redirect('register')
        password = form.cleaned_data.get('password')
        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        login(request, new_user)
        return redirect('index')
    register = 'register'
    return render(request, 'userpage.html', context={'form': form, 'register': register})

def loginUser(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        if user is not None:
            login(request, user)
            return redirect('index')
        elif User.objects.filter(username = form.cleaned_data.get('username')):
            messages.warning(request, 'Şifrə yanlışdır səhvdir')
            return render(request, 'userpage.html', context={'form': form})
        else:
            messages.warning(request, 'İstifadəçi adı səhvdir')
            return render(request, 'userpage.html', context={'form': form})
    return render(request, 'userpage.html', context={'form': form})

@login_required(login_url='/user/login/')
def logoutUser(request):
    logout(request)
    return redirect("index")

@login_required(login_url='/user/login/')
def changeUser(request):
    change_form = UserUpdateForm(request.POST or None, instance=request.user)
    if change_form.is_valid():
        change_form.save()
        messages.success(request,'Uğurla dəyişdirildi')
        return redirect('/article/userDashboard/')
    return render(request,'userChange.html', context={'change_form':change_form})

@login_required(login_url='/user/login/')
def changePassword(request):
    if request.method == 'POST':
        passwordChange_form = PasswordChangeForm(request.user , request.POST )
        if passwordChange_form.is_valid():
            user = passwordChange_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifrə uğurla yeniləndi')
            return redirect('/article/userDashboard/')
        else:
            messages.error(request, "Xəta baş verdi")
            return render(request, 'userChange.html', context={'passwordChange_form':passwordChange_form} )
    else:
        passwordChange_form = PasswordChangeForm(request.user )
        return render(request, 'userChange.html', context={'passwordChange_form':passwordChange_form} )
