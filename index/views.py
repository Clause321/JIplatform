from django.shortcuts import render_to_response
from activity.models import Activity
from django import forms
from django.contrib.auth.forms import UserCreationForm

def index(request):
    news = Activity.objects.filter(type='news').order_by('write_date')[:6]
    activity = Activity.objects.filter(type='activity').order_by('write_date')[:6]
    announce = Activity.objects.filter(type='announce').order_by('write_date')[:6]
    #need reverse write_date
    return render_to_response('index.html', {'news': news,
                                             'activity': activity,
                                             'announce': announce,
                                             })

def test(request):
    form = UserCreationForm();
    return render_to_response('test.html', {'form': form})