from django.shortcuts import render_to_response
from activity.models import Activity

def index(request):
    news = Activity.objects.order_by('write_date')#[:6]
    return render_to_response('index.html', {'news': news})
