from django import forms

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
