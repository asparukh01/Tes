from django.contrib import admin
from django.db.models import fields
from headhunter_app.models import *

# Register your models here.
class TodoTask_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    fields = ['title','description', 'status', 'updated_at', 'created_at']
    readonly_fields = ['updated_at', 'created_at']

# admin.site.register(TodoTask, TodoTask_Admin)
admin.site.register(Resume)
admin.site.register(Vacancy)
admin.site.register(Info)
admin.site.register(Experience)
admin.site.register(Category)

