from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "full_name", "email", "phone", "faculty", "group", "university")
    search_fields = ("student_id", "full_name", "email", "phone")
    list_filter = ("faculty", "group", "university")
    list_select_related = True