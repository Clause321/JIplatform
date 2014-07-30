from django.forms import ModelForm
from django import forms
from activity.models import Activity

class ActivityForm(ModelForm):
    pic = forms.ImageField()
    class Meta:
        model = Activity
        fields = [ 'title','due_date', 'content', 'summary', 'pic', 'type']