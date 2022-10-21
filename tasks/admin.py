from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    #Mostrar los campos de solo lectura
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Task, TaskAdmin)
