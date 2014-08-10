from django.shortcuts import render_to_response
from activity.models import Activity, act_allow_group
from activity.forms import ActivityForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.core.context_processors import csrf
from group.models import Group as Grp
from django.contrib.auth.models import Group, User
from django import forms
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
        # using filter form, still need modification for js
        current_num = int(request.POST['aaa'])
        new = activityFilterForm(request.POST) # is this line right?
        new = new.acFilter()
        new = new[current_num:current_num+4]
        json = serializers.serialize('json', new)
        return HttpResponse(json)
    else:
        ac = activityFilterForm()

        if typeOrGroup == 'type':
            ac.type = name;
        elif typeOrGroup == 'group':
            #need to check permission for seek
            ac.group = name;

        ac.acFilter()
        ac = ac[:6]
        return render_to_response('actlist.html', {'activities': ac})

class activityFilterForm(forms.Form):
    ac = Activity.objects.all()

    type = forms.CharField(label='type', max_length=20)
    group = forms.CharField(label='group', max_length=20)
    seek = forms.BooleanField()

    title = forms.CharField(label='title', max_length=30)

    def acFilter(self):
        if 'type' in self:
            self.ac = self.ac.filter(type = self.type)
        if 'group' in self:
            self.ac = self.ac.filter(group = self.group)
        if not 'seek' in self:   # do not include activities already due
            self.ac.filter(due_date__gte = datetime.datetime.now()) # naive datetime?

        if 'title' in self:  # search title
            self.ac = self.ac.filter(title__icontains = self.title)

        self.ac = self.ac.order_by('-write_date')

    # may add group filter to obtain seeked or unseeked activities for different groups



def activity_page(request, ID):
    # need to check permission if private
    activity = Activity.objects.get(id=ID)
    return render_to_response('actcontent.html', {'activity': activity})


