from django.contrib import admin
from .models import Department, Applicant, Service, Application


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "phone")
    search_fields = ("name", "address")


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("id", "surname", "name", "patronymic", "birth_date", "document_number", "phone")
    search_fields = ("surname", "name", "patronymic", "document_number", "phone")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "processing_days", "price")
    search_fields = ("name",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "applicant", "service", "employee", "department", "created_date", "status")
    list_filter = ("status", "service", "department", "created_date")
    search_fields = (
        "applicant__surname",
        "applicant__name",
        "applicant__document_number",
        "service__name",
    )