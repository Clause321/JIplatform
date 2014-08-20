from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from group.models import Group
from django.contrib.auth.models import User, Group as grp
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods


# Create your views here.


def group(request):
    return render_to_response('group.html')

def group_choose(request):
    if 'group_staff' in request.user.groups['name']:
        groups = Group.objects.all()
        return render_to_response('groupchoose.html', {'groups': groups})
    else:
        return HttpResponse('You have not the permission to access this page')

def ctrl_group(request, group):
    if not group in request.user.groups['name']:
        return HttpResponse('You have not the permission to access this page')
    else:
        applying_users = User.objects.filter(groups__name=group+'_apply')
        staff_users = User.objects.filter(groups__name=group+'_staff')
        ordinary_users = User.objects.filter(groups__name=group).exclude(groups__name=group+'_staff')
        return render_to_response('groupctrl.html', locals())

@require_http_methods(["POST"]) # user_id, action, status
def ctrl_group_action(request, group):
    if not group in request.user.groups['name']:
        return HttpResponse('You have not the permission to access this page')
    else:
        user = User.objects.get(id = request.POST['id'])
        action = request.POST['action']
        status = request.POST['status']
        if action == 'add':
            user.groups.delete(name = group+'_apply')
            user.groups.add(name = group)
        elif action == 'delete':
            if status == 'apply':
                user.groups.delete(name = group+'_apply')
            elif status == 'staff':
                user.groups.delete(name = group+'_staff', name = group)
                # check if the user is still a group staff
            elif status == 'ordinary':
                user.groups.delete(name = group)
        elif action == 'make_staff':
            user.groups.add(name = group+'_staff')
        elif action == 'make_ordinary':
            user.groups.delete(name = group+'_staff')
        user.save()
        return # redirect to previous page

def apply_group(request):
    error = ''
    if request.method == 'POST':
        choice = request.POST['group']
        try:
            g = grp.objects.get(name = choice)
            ga = grp.objects.get(name = choice+'_apply')
        except:
            error = 'the chosen group does not exist'
        if g in request.user.group:
            error = 'you are already a member'
        elif ga in request.user.group:
            error = 'you have already applied this group'
        else:
            return HttpResponseRedirect('success/')
    groups = Group.objects.all()

    return render_to_response('applygroup.html', {'groups': groups, 'error': error})

@staff_member_required
def create_group(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success/')
    else:
        form = GroupCreationForm()
    return render_to_response('creategroup.html', {'form': form})

class GroupCreationForm(forms.ModelForm):
    error_messages = {
        'invalid_nature': "The nature of the group is invalid.",
        'userDoesNotExist': "The staffuser you choose does not exist.",
    }

    staffname = forms.CharField(max_length = 30) # should be 'SU', 'club' or 'other'

    class Meta:
        model = Group
        fields = ['name', 'title', 'nature']

    def clean_nature(self):
        nature = self.cleaned_data['nature']
        if not nature in ['SU', 'club', 'other']:
            raise forms.ValidationError(
                self.error_messages['invalid_nature'],
                code='invalid_nature',
            )
        return nature

    def clean_staffname(self):
        staffname = self.cleaned_data['staffname']
        try:
            User.objects.get(username=staffname)
        except:
            raise forms.ValidationError(
                self.error_messages['userDoesNotExist'],
                code='userDoesNotExist',
            )
        return staffname

    def save(self, commit=True):
        group = super(GroupCreationForm, self).save(commit=False)
        if commit:
            group.save()
            # create three groups: one is the staff another is the apply on waiting list
            title = self.cleaned_data['title']
            title_staff = title+'_staff'
            title_apply = title+'_apply'
            newgrp = grp(name=title)
            newgrp.save()
            newgrp_staff = grp(name=title_staff)
            newgrp_staff.save()
            newgrp_apply = grp(name=title_apply)
            newgrp_apply.save()
            # make the staff a member and a staff member
            staffname = self.cleaned_data['staffname']
            staff = User.objects.get(username=staffname)
            staff.group.add(newgrp, newgrp_staff)
            staff.save()
            # make the user a staff
            g = grp.objects.get(name='group_staff')
            if g not in staff.group:
                staff.group.add(g)
                staff.save()
        return group






