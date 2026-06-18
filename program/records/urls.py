from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("applicants/", views.applicants_list, name="applicants_list"),
    path("applicants/add/", views.applicant_create, name="applicant_create"),
    path("applicants/<int:pk>/edit/", views.applicant_update, name="applicant_update"),

    path("applications/", views.applications_list, name="applications_list"),
    path("applications/add/", views.application_create, name="application_create"),
    path("applications/<int:pk>/edit/", views.application_update, name="application_update"),
    path("applications/<int:pk>/status/", views.application_update_status, name="application_update_status"),
    path("applications/<int:pk>/delete/", views.application_delete, name="application_delete"),

    path("statistics/", views.statistics, name="statistics"),
    path("reports/applications/", views.applications_report, name="applications_report"),
    path("services/", views.services_list, name="services_list"),
    path("about/", views.about_system, name="about_system"),
]