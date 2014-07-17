from django.contrib import admin
from activity.models import Activity

# class ActivityAdmin(admin.ModelAdmin):
#     list_display = ('id',)
# admin.site.register(Activity, ActivityAdmin)
admin.site.register(Activity)
