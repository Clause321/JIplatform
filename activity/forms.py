from django.forms import ModelForm
from activity.models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        include = [ 'title','due_date', 'content', 'summary']