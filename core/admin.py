from django.contrib import admin
from .models import Student, StudentService, AcademicDebt, ResearchService, InternationalService, FinanceService

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "full_name", "email", "phone", "faculty", "group", "university")
    search_fields = ("student_id", "full_name", "email", "phone")
    list_filter = ("faculty", "group", "university")
    list_select_related = True

@admin.register(StudentService)
class StudentServiceAdmin(admin.ModelAdmin):
    list_display = ("student", "request_type", "request_date", "status")
    search_fields = ("student__full_name", "request_type")
    list_filter = ("status", "request_type")

@admin.register(AcademicDebt)
class AcademicDebtAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "debt_amount", "retake_status", "created_at")
    search_fields = ("student__full_name", "subject")
    list_filter = ("retake_status",)

@admin.register(ResearchService)
class ResearchServiceAdmin(admin.ModelAdmin):
    list_display = ("student", "service_type", "request_date", "status")
    search_fields = ("student__full_name", "service_type")
    list_filter = ("status", "service_type")

@admin.register(InternationalService)
class InternationalServiceAdmin(admin.ModelAdmin):
    list_display = ("student", "service_type", "request_date", "status")
    search_fields = ("student__full_name", "service_type")
    list_filter = ("status", "service_type")

@admin.register(FinanceService)
class FinanceServiceAdmin(admin.ModelAdmin):
    list_display = ("student", "service_type", "amount", "request_date", "status")
    search_fields = ("student__full_name", "service_type")
    list_filter = ("status", "service_type")