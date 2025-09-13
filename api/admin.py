# api/admin.py
from django.contrib import admin
from .models import User, Project, Sprint, Task, Incident, Comment

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(Incident)
admin.site.register(Comment)
