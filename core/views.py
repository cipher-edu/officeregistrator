from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, StudentForm, StudentServiceForm, AcademicDebtForm, ResearchServiceForm, InternationalServiceForm, FinanceServiceForm
from .utils import save_student_to_db
from .models import Student, StudentService, AcademicDebt, ResearchService, InternationalService, FinanceService

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

def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form})

@login_required(login_url="student_login")
def student_service_list(request):
    """List student services for the logged-in student."""
    student_id = request.session.get("student_id")
    services = StudentService.objects.filter(student__student_id=student_id)
    return render(request, 'core/student_service_list.html', {'services': services})

@login_required(login_url="student_login")
def student_service_create(request):
    """Allow logged-in students to create a service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = StudentServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('student_service_list')
    else:
        form = StudentServiceForm()

    return render(request, 'core/student_service_form.html', {'form': form})

def student_service_update(request, pk):
    service = get_object_or_404(StudentService, pk=pk)
    if request.method == 'POST':
        form = StudentServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('student_service_list')
    else:
        form = StudentServiceForm(instance=service)
    return render(request, 'core/student_service_form.html', {'form': form})

@login_required(login_url="student_login")
def academic_debt_list(request):
    """List academic debts for the logged-in student."""
    student_id = request.session.get("student_id")
    debts = AcademicDebt.objects.filter(student__student_id=student_id)
    return render(request, 'core/academic_debt_list.html', {'debts': debts})

@login_required(login_url="student_login")
def academic_debt_create(request):
    """Allow logged-in students to create an academic debt request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = AcademicDebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.student = student  # Automatically associate the logged-in student
            debt.save()
            return redirect('academic_debt_list')
    else:
        form = AcademicDebtForm()

    return render(request, 'core/academic_debt_form.html', {'form': form})

def academic_debt_update(request, pk):
    debt = get_object_or_404(AcademicDebt, pk=pk)
    if request.method == 'POST':
        form = AcademicDebtForm(request.POST, instance=debt)
        if form.is_valid():
            form.save()
            return redirect('academic_debt_list')
    else:
        form = AcademicDebtForm(instance=debt)
    return render(request, 'core/academic_debt_form.html', {'form': form})

@login_required(login_url="student_login")
def research_service_list(request):
    """List research services for the logged-in student."""
    student_id = request.session.get("student_id")
    services = ResearchService.objects.filter(student__student_id=student_id)
    return render(request, 'core/research_service_list.html', {'services': services})

@login_required(login_url="student_login")
def research_service_create(request):
    """Allow logged-in students to create a research service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = ResearchServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('research_service_list')
    else:
        form = ResearchServiceForm()

    return render(request, 'core/research_service_form.html', {'form': form})

def research_service_update(request, pk):
    service = get_object_or_404(ResearchService, pk=pk)
    if request.method == 'POST':
        form = ResearchServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('research_service_list')
    else:
        form = ResearchServiceForm(instance=service)
    return render(request, 'core/research_service_form.html', {'form': form})

@login_required(login_url="student_login")
def international_service_list(request):
    """List international services for the logged-in student."""
    student_id = request.session.get("student_id")
    services = InternationalService.objects.filter(student__student_id=student_id)
    return render(request, 'core/international_service_list.html', {'services': services})

@login_required(login_url="student_login")
def international_service_create(request):
    """Allow logged-in students to create an international service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = InternationalServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('international_service_list')
    else:
        form = InternationalServiceForm()

    return render(request, 'core/international_service_form.html', {'form': form})

def international_service_update(request, pk):
    service = get_object_or_404(InternationalService, pk=pk)
    if request.method == 'POST':
        form = InternationalServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('international_service_list')
    else:
        form = InternationalServiceForm(instance=service)
    return render(request, 'core/international_service_form.html', {'form': form})

@login_required(login_url="student_login")
def finance_service_list(request):
    """List finance services for the logged-in student."""
    student_id = request.session.get("student_id")
    services = FinanceService.objects.filter(student__student_id=student_id)
    return render(request, 'core/finance_service_list.html', {'services': services})

def finance_service_create(request):
    if request.method == 'POST':
        form = FinanceServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance_service_list')
    else:
        form = FinanceServiceForm()
    return render(request, 'core/finance_service_form.html', {'form': form})

def finance_service_update(request, pk):
    """Update a finance service request."""
    service = get_object_or_404(FinanceService, pk=pk)
    if request.method == 'POST':
        form = FinanceServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('finance_service_list')
    else:
        form = FinanceServiceForm(instance=service)
    return render(request, 'core/finance_service_form.html', {'form': form})

@login_required(login_url="student_login")
def submit_student_service(request):
    """Allow logged-in students to submit a service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = StudentServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('student_dashboard')
    else:
        form = StudentServiceForm()

    return render(request, 'core/submit_student_service.html', {'form': form})

@login_required(login_url="student_login")
def submit_academic_debt(request):
    """Allow logged-in students to submit an academic debt request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = AcademicDebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.student = student  # Automatically associate the logged-in student
            debt.save()
            return redirect('student_dashboard')
    else:
        form = AcademicDebtForm()

    return render(request, 'core/submit_academic_debt.html', {'form': form})

@login_required(login_url="student_login")
def submit_research_service(request):
    """Allow logged-in students to submit a research service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = ResearchServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('student_dashboard')
    else:
        form = ResearchServiceForm()

    return render(request, 'core/submit_research_service.html', {'form': form})

@login_required(login_url="student_login")
def submit_international_service(request):
    """Allow logged-in students to submit an international service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = InternationalServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('student_dashboard')
    else:
        form = InternationalServiceForm()

    return render(request, 'core/submit_international_service.html', {'form': form})

@login_required(login_url="student_login")
def submit_finance_service(request):
    """Allow logged-in students to submit a finance service request."""
    student_id = request.session.get("student_id")
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = FinanceServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.student = student  # Automatically associate the logged-in student
            service.save()
            return redirect('student_dashboard')
    else:
        form = FinanceServiceForm()

    return render(request, 'core/submit_finance_service.html', {'form': form})