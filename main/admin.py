from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Report)
admin.site.register(ProcessReport)
admin.site.register(Supervisor)
admin.site.register(Profile)
admin.site.register(ProjectStatus)
admin.site.register(SuggesstedProjects)