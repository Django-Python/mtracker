from django.contrib import admin
from .models import TaskData

class TASKDATA(admin.ModelAdmin):
    disp_field = ("EmpID", "EmpName", "EmpEmail", "TaskName", "TaskStatus", "TaskSummary")
admin.site.register(TaskData, TASKDATA)
# Register your models here.
