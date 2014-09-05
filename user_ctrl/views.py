from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
import json as xjson

def register(request):
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        # username, password1, password2
        if new_user.is_valid():
            new_user.save()
            response_data = {}
            response_data['message'] = 'success'
            return HttpResponse(xjson.dumps(response_data), content_type="application/json")
        error = new_user.errors.as_json()
        return HttpResponse(error, content_type="application/json")
    return HttpResponse('Please use post method')

def login_view(request):
    error = ''
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],
                        password = request.POST['password'])
        response_data = {}
        if user is not None:
            if user.is_active:
                login(request, user)
                response_data['message'] = 'success'
                return HttpResponse(xjson.dumps(response_data), content_type="application/json")
            else:
                error = "The account has been disabled"
        else:
            error = "The username and password were incorrect."
        response_data['message'] = error
        return HttpResponse(xjson.dumps(response_data), content_type="application/json")
    return HttpResponse('Please use post method')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
