from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        error = new_user.get_validation_errors()
        if not error:
            new_user.save()
            return HttpResponseRedirect('/login/')

    return render_to_response('register.html', {'error': error})

def login_view(request):
    error = 0
    if request.method == 'POST':
        user = AuthenticationForm(request.POST)
        error = user.get_validation_errors()
        if not error:
            login(request, user)
            return HttpResponseRedirect('/index/')

    return render_to_response('longin.html', {'error': error})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')
