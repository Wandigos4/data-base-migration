from django import forms
from .models import Applicant, Application


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [
            "surname",
            "name",
            "patronymic",
            "birth_date",
            "document_number",
            "phone",
            "address",
        ]

        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "applicant",
            "service",
            "department",
            "created_date",
            "status",
            "note",
        ]

        widgets = {
            "created_date": forms.DateInput(attrs={"type": "date"}),
        }


class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "status",
            "note",
        ]