from django.contrib import admin
from .models import Scheduling

# Register your models here.
@admin.register(Scheduling)
class SchedullingAdmin(admin.ModelAdmin):
    list_display = ['patient','exam', 'status', 'scheduled_to']
