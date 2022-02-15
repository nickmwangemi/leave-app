from django.contrib import admin

from .models import LeaveRequest


class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ["name", "start_date", "end_date", "type_of_leave", "count_workdays"]
    list_editable = ["start_date", "end_date", "type_of_leave"]



admin.site.register(LeaveRequest, LeaveRequestAdmin)
