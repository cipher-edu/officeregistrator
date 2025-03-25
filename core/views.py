from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .utils import save_student_to_db
from .models import *
def student_login(request):
    """Talabaning tizimga kirish sahifasi"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login_data = form.cleaned_data["login"]
            password = form.cleaned_data["password"]

            student = save_student_to_db(login_data, password)  # ✅ API orqali ma'lumot olish
            if student:
                user, created = User.objects.get_or_create(username=student.student_id)
                login(request, user)
                
                # 🔵 Kirgan foydalanuvchini sessionga saqlash
                request.session["student_id"] = student.student_id  

                return redirect("student_dashboard")  # ✅ Dashboard sahifasiga yo‘naltirish
            else:
                return render(request, "login.html", {"form": form, "error": "Login yoki parol noto‘g‘ri!"})
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})

def student_logout(request):
    """Talabaning tizimdan chiqishi"""
    logout(request)
    request.session.flush()  # 🔴 Sessionni tozalash
    return redirect("student_login")  # ✅ Logout bo‘lgandan keyin login sahifasiga yo‘naltirish


# def student_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             login = form.cleaned_data["login"]
#             password = form.cleaned_data["password"]

#             student = save_student_to_db(login, password)
#             if student:
#                 return redirect("student_dashboard")  # Muvaffaqiyatli kirish
#             else:
#                 return render(request, "login.html", {"form": form, "error": "Login yoki parol noto‘g‘ri!"})
#     else:
#         form = LoginForm()
    
#     return render(request, "login.html", {"form": form})


@login_required(login_url="student_login")
def student_dashboard(request):
    """Dashboardda login qilgan foydalanuvchining ma'lumotlari va baholari"""
    student_id = request.session.get("student_id")

    if student_id:
        student = Student.objects.filter(student_id=student_id).first()

    else:
        student = None
        subjects = []

    return render(request, "dashboard.html", {"student": student})