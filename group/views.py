from django.shortcuts import render
from django.shortcuts import render_to_response
from activity.models import Activity
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def group(request):
    return render_to_response('group.html')