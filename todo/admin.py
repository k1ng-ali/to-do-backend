from django.contrib import admin
from todo.models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "session_key", "create_at")
    list_filter = ("status", "create_at")
    search_fields = ("title", "description")