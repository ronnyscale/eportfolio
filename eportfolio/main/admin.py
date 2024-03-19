from django.contrib import admin
from .models import Student, Achievement


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'location', 'email', 'description')
    list_filter = ('first_name', 'last_name', 'location', 'email', 'description')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'description', 'location')
    list_filter = ('student', 'title', 'description', 'location')