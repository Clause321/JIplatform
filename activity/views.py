from django.shortcuts import render_to_response
from activity.models import Activity
from activity.forms import ActivityForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.core.context_processors import csrf
import datetime

def write_news(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            n = form.save(commit = False)
            n.write_date = datetime.datetime.now()
            n.due_date = datetime.datetime.now()
            n.group = 'news'
            n.save()
            return HttpResponseRedirect('/news/')
    else:
        form = ActivityForm()
    return render_to_response('pushact.html', {'form': form})

def news(request):
    if request.method =='POST':
        c = {}
        c.update(csrf(request))
        #current_num = int(request.POST['i'])
        #new = Activity.objects.filter(group='news')[current_num:current_num+4]
        #json = serializers.serialize('json', new)
        new = Activity.objects.filter(group='news')[:4]
        json = serializers.serialize('json', new)
        return HttpResponse(json)
    else:
        activities = Activity.objects.filter(group='news')[:6]
        return render_to_response('actlist.html', {'activities', activities})

def activity_page(request, ID):
    activity = Activity.objects.get(itemID=ID)
    return render_to_response('actcontent.html', {'activity': activity})


