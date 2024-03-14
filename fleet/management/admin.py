from django.contrib import admin

# Register your models here.
from management.models import taxis, trajectories  

# Register your models here.
admin.site.register(taxis)
admin.site.register(trajectories)