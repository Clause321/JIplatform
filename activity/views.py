from django.shortcuts import render_to_response
from activity.models import Activity, act_allow_group, act_group
from activity.forms import ActivityForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.core.context_processors import csrf
from group.models import Group as Grp
from django.contrib.auth.models import Group, User
import datetime

def write_act(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            # activity
            n = form.save(commit = False)
            n.write_date = datetime.datetime.now()
            n.save()
            # group
            g = act_group()
            g.act_id = n.id
            g.group_id = Grp.objects.get(name = form.group)
            g.save()
            # allow_group
            # to be done
            return HttpResponseRedirect('/write/')
    else:
        form = ActivityForm()
    return render_to_response('pushact.html', {'form': form})

def activity(request, typeOrGroup, name):
    if request.method =='POST':         # to be done
        #current_num = int(request.POST['i'])
        #new = Activity.objects.filter(group='news')[current_num:current_num+4]
        #json = serializers.serialize('json', new)
        new = Activity.objects.filter(group='news')[:4]
        json = serializers.serialize('json', new)
        return HttpResponse(json)
    else:
        if typeOrGroup == 'type':
            activities = Activity.objects.filter(type = name)[:6]
        elif typeOrGroup == 'group':
            activities = Activity.objects.filter(group = name)[:6]
        return render_to_response('actlist.html', {'activities', activities})

def activity_page(request, ID):
    activity = Activity.objects.get(id=ID)
    return render_to_response('actcontent.html', {'activity': activity})


