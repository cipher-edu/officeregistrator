from django import forms
from .models import Student, StudentService, AcademicDebt, ResearchService, InternationalService, FinanceService

class LoginForm(forms.Form):
    login = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Login"}),
        label="Login"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Parol"}),
        label="Parol"
    )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentServiceForm(forms.ModelForm):
    class Meta:
        model = StudentService
        exclude = ['student', 'status']  # Exclude the student and status fields
        widgets = {
            'request_type': forms.Select(attrs={"class": "form-control"}),
            'response': forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class AcademicDebtForm(forms.ModelForm):
    class Meta:
        model = AcademicDebt
        exclude = ['student', 'retake_status']  # Exclude the student and status fields
        widgets = {
            'subject': forms.TextInput(attrs={"class": "form-control"}),
            'debt_amount': forms.NumberInput(attrs={"class": "form-control"}),
        }

class ResearchServiceForm(forms.ModelForm):
    class Meta:
        model = ResearchService
        exclude = ['student', 'status']  # Exclude the student and status fields
        widgets = {
            'service_type': forms.Select(attrs={"class": "form-control"}),
            'details': forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class InternationalServiceForm(forms.ModelForm):
    class Meta:
        model = InternationalService
        exclude = ['student', 'status']  # Exclude the student and status fields
        widgets = {
            'service_type': forms.Select(attrs={"class": "form-control"}),
            'response': forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

class FinanceServiceForm(forms.ModelForm):
    class Meta:
        model = FinanceService
        exclude = ['student', 'status']  # Exclude the student and status fields
        widgets = {
            'service_type': forms.Select(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control"}),
        }
