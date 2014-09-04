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
        if new.is_valid():
            new.acFilter()
            json = serializers.serialize('json', new.ac[current_num:current_num+4])
            return HttpResponse(json)
        else:
            return HttpResponse('The post data is not valid!')
    else:
        ac = activityFilterForm()

        ac.full_clean()
        if typeOrGroup == 'type':
            ac.typeFilter(name);
        elif typeOrGroup == 'group':
            #need to check permission for seek
            ac.groupFilter(name);
        ac.acFilter()
        return render_to_response('actlist.html', {'activities': ac.ac[:6]})

class activityFilterForm(forms.Form):
    aaa = forms.IntegerField(required = False)
    ac = Activity.objects.all()

    type = forms.CharField(label='type', max_length=20, required = False)
    group = forms.CharField(label='group', max_length=20, required = False)
    seek = forms.BooleanField(required = False)

    title = forms.CharField(label='title', max_length=30, required = False)

    def acFilter(self):
        if 'type' in self.data:
            self.ac = self.ac.filter(type = self.cleaned_data['type'])
        if 'group' in self.data:
            self.ac = self.ac.filter(group = self.cleaned_data['group'])
        if not 'seek' in self.data:   # do not include activities already due
            self.ac.filter(due_date__gte = datetime.datetime.now()) # naive datetime?

        if 'title' in self.data:  # search title
            self.ac = self.ac.filter(title__icontains = self.cleaned_data['title'])

        self.ac = self.ac.order_by('-write_date')

    # may add group filter to obtain seeked or unseeked activities for different groups

    def typeFilter(self, type):
        self.ac = self.ac.filter(type = type)

    def groupFilter(self, group):
        self.ac = self.ac.filter(group = group)



def activity_page(request, ID):
    # need to check permission if private
    activity = Activity.objects.get(id=ID)
    return render_to_response('actcontent.html', {'activity': activity})


