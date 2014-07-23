from django.forms import ModelForm
from activity.models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = [ 'title','due_date', 'content', 'summary', 'pic',]