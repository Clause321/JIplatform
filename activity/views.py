from django.shortcuts import render_to_response
from activity.models import Activity, act_allow_group
from activity.forms import ActivityForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.core.context_processors import csrf
from group.models import Group as Grp
from django.contrib.auth.models import Group, User
import datetime

def write_act(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            # activity
            n = form.save(commit = False)
            n.write_date = datetime.datetime.now()
            n.save()
            #the line below should be uncommented when user is added
            #n.writer_id = request.user.id


            # allow_group
            # to be done
            return HttpResponseRedirect('/write/')
    else:
        form = ActivityForm()
    return render_to_response('pushact.html', {'form': form})

def activity(request, typeOrGroup, name):
    if request.method =='POST':
        # add_more function, not complete for group. Should use filter form.
        current_num = int(request.POST['aaa'])
        new = Activity.objects.filter(type = 'news').order_by('-write_date')[current_num:current_num+4]
        json = serializers.serialize('json', new)
        return HttpResponse(json)
    else:
        if typeOrGroup == 'type':
            activities = Activity.objects.filter(type = name).order_by('-write_date')[:6]
        elif typeOrGroup == 'group':
            activities = Activity.objects.filter(group = name).order_by('-write_date')[:6]
        return render_to_response('actlist.html', {'activities': activities})

def activity_page(request, ID):
    # need to check permission if private
    activity = Activity.objects.get(id=ID)
    return render_to_response('actcontent.html', {'activity': activity})


