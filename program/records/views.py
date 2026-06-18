from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Applicant, Application, Service, Department
from .forms import ApplicantForm, ApplicationForm, ApplicationStatusForm


@login_required
def dashboard(request):
    context = {
        "applicants_count": Applicant.objects.count(),
        "applications_count": Application.objects.count(),
        "services_count": Service.objects.count(),
        "departments_count": Department.objects.count(),
        "new_applications_count": Application.objects.filter(status="new").count(),
        "completed_applications_count": Application.objects.filter(status="completed").count(),
    }

    return render(request, "records/dashboard.html", context)


@login_required
def applicants_list(request):
    query = request.GET.get("q", "")

    applicants = Applicant.objects.all().order_by("surname")

    if query:
        applicants = (
            Applicant.objects.filter(surname__icontains=query)
            | Applicant.objects.filter(name__icontains=query)
            | Applicant.objects.filter(document_number__icontains=query)
        )

    context = {
        "applicants": applicants,
        "query": query,
    }

    return render(request, "records/applicants_list.html", context)


@login_required
def applications_list(request):
    status = request.GET.get("status", "")

    applications = Application.objects.all().order_by("-created_date")

    if status:
        applications = applications.filter(status=status)

    context = {
        "applications": applications,
        "status": status,
        "status_choices": Application.STATUS_CHOICES,
    }

    return render(request, "records/applications_list.html", context)


@login_required
def statistics(request):
    status_stats = []

    for value, label in Application.STATUS_CHOICES:
        count = Application.objects.filter(status=value).count()
        status_stats.append({
            "label": label,
            "count": count,
        })

    service_stats = Service.objects.annotate(
        applications_count=Count("application")
    )

    context = {
        "status_stats": status_stats,
        "service_stats": service_stats,
        "total_applicants": Applicant.objects.count(),
        "total_applications": Application.objects.count(),
        "total_services": Service.objects.count(),
        "total_departments": Department.objects.count(),
    }

    return render(request, "records/statistics.html", context)


@login_required
def applicant_create(request):
    if request.method == "POST":
        form = ApplicantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("applicants_list")
    else:
        form = ApplicantForm()

    context = {
        "form": form,
    }

    return render(request, "records/applicant_form.html", context)


@login_required
def application_create(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.employee = request.user
            application.save()
            return redirect("applications_list")
    else:
        form = ApplicationForm()

    context = {
        "form": form,
    }

    return render(request, "records/application_form.html", context)
@login_required
def application_update_status(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if request.method == "POST":
        form = ApplicationStatusForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect("applications_list")
    else:
        form = ApplicationStatusForm(instance=application)

    context = {
        "form": form,
        "application": application,
    }

    return render(request, "records/application_status_form.html", context)
@login_required
def applications_report(request):
    status = request.GET.get("status", "")

    applications = Application.objects.all().order_by("-created_date")

    if status:
        applications = applications.filter(status=status)

    context = {
        "applications": applications,
        "status": status,
        "status_choices": Application.STATUS_CHOICES,
        "total_count": applications.count(),
    }

    return render(request, "records/applications_report.html", context)

@login_required
def services_list(request):
    services = Service.objects.all().order_by("name")

    context = {
        "services": services,
    }

    return render(request, "records/services_list.html", context)

@login_required
def applicant_update(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)

    if request.method == "POST":
        form = ApplicantForm(request.POST, instance=applicant)

        if form.is_valid():
            form.save()
            return redirect("applicants_list")
    else:
        form = ApplicantForm(instance=applicant)

    context = {
        "form": form,
        "applicant": applicant,
    }

    return render(request, "records/applicant_form.html", context)

@login_required
def applicant_update(request, pk):
    applicant = get_object_or_404(Applicant, pk=pk)

    if request.method == "POST":
        form = ApplicantForm(request.POST, instance=applicant)

        if form.is_valid():
            form.save()
            return redirect("applicants_list")
    else:
        form = ApplicantForm(instance=applicant)

    context = {
        "form": form,
        "applicant": applicant,
    }

    return render(request, "records/applicant_form.html", context)

@login_required
def application_update(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)

        if form.is_valid():
            updated_application = form.save(commit=False)
            updated_application.employee = application.employee
            updated_application.save()
            return redirect("applications_list")
    else:
        form = ApplicationForm(instance=application)

    context = {
        "form": form,
        "application": application,
    }

    return render(request, "records/application_form.html", context)

@login_required
def application_delete(request, pk):
    application = get_object_or_404(Application, pk=pk)

    if request.method == "POST":
        application.delete()
        return redirect("applications_list")

    context = {
        "application": application,
    }

    return render(request, "records/application_confirm_delete.html", context)

@login_required
def about_system(request):
    return render(request, "records/about_system.html")