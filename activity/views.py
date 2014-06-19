from django.shortcuts import render_to_response
from activity.forms import ActivityForm
from django.http import HttpResponseRedirect

def write_news(request):
    if request.method == 'POST':
        form = ActivityForm(request)
        if form.is_valid():
            form.save(group = 'news')
            return HttpResponseRedirect('/news/')
    else:
        form = ActivityForm()
    return render_to_response('pushact.html', {'form': form})