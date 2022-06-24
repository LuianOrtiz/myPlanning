from django.contrib import admin
from apps.todolist.models import List, Task, Step
# Register your models here.

admin.site.register(List)
admin.site.register(Task)
admin.site.register(Step)
