from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def register(request):
    error = {'username': '', 'password1': '', 'password2': ''}
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        # username, password1, password2
        if new_user.isValid():
            new_user.save()
            return HttpResponseRedirect('/login/')
        error = new_user.error

    return render_to_response('register.html', {'error': error})

def login_view(request):
    error = {'username': '', 'password': ''}
    if request.method == 'POST':
        user = AuthenticationForm(request.POST)
        # username, password
        if user.isValid():
            login(request, user)
            return HttpResponseRedirect('/index/')
        error = user.error

    return render_to_response('longin.html', {'error': error})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')
