from django.shortcuts import render, redirect
from .forms import LoginForm
from .utils import save_student_to_db  # Student API bilan ishlash funksiyasi
from .models import Student
def student_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data["login"]
            password = form.cleaned_data["password"]

            student = save_student_to_db(login, password)
            if student:
                return redirect("student_dashboard")  # Muvaffaqiyatli kirish
            else:
                return render(request, "login.html", {"form": form, "error": "Login yoki parol noto‘g‘ri!"})
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})
from django.shortcuts import render

def student_dashboard(request):
    student = Student.objects.last()  # ✅ Eng oxirgi kirgan talabani olish
    return render(request, "dashboard.html", {"student": student})