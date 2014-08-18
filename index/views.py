from django.shortcuts import render_to_response
from activity.models import Activity
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext # need to apply for all views

def index(request):
    news = Activity.objects.filter(type='news').order_by('-write_date')[:6]
    activity = Activity.objects.filter(type='activity').order_by('-write_date')[:6]
    announce = Activity.objects.filter(type='announce').order_by('-write_date')[:6]
    return render_to_response('index.html', {'news': news,
                                             'activity': activity,
                                             'announce': announce,
                                             }, context_instance=RequestContext(request))

def test(request):
    form = UserCreationForm();
    return render_to_response('test.html', {'form': form})