from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def register(request):
    error = {'username': '', 'password1': '', 'password2': ''}
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        # username, password1, password2
        if new_user.is_valid():
            new_user.save()
            return HttpResponseRedirect('/login/')
        error = new_user.errors

    return HttpResponseRedirect('/', {'register_error': error}) # should use js to pass error message

def login_view(request):
    error = ''
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],
                        password = request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = "The account has been disabled"
        else:
            error = "The username and password were incorrect."
        return HttpResponseRedirect('/', {'login_error': error}) # should use js to pass error message

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
