from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True, verbose_name="Talaba ID")
    full_name = models.CharField(max_length=200, verbose_name="To'liq ismi")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefon")
    faculty = models.CharField(max_length=200, null=True, blank=True, verbose_name="Fakultet")
    group = models.CharField(max_length=100, null=True, blank=True, verbose_name="Guruh")
    university = models.CharField(max_length=200, null=True, blank=True, verbose_name="Universitet")
    specialty = models.CharField(max_length=200, null=True, blank=True, verbose_name="Mutaxassislik")
    birth_date = models.CharField(max_length=20, null=True, blank=True, verbose_name="Tug'ilgan sana")
    passport_pin = models.CharField(max_length=20, null=True, blank=True, verbose_name="Pasport PIN")
    passport_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Pasport raqami")
    gender = models.CharField(max_length=10, null=True, blank=True, verbose_name="Jinsi")
    education_form = models.CharField(max_length=50, null=True, blank=True, verbose_name="Ta'lim shakli")
    education_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Ta'lim turi")
    payment_form = models.CharField(max_length=50, null=True, blank=True, verbose_name="To'lov shakli")
    address = models.TextField(null=True, blank=True, verbose_name="Manzil")
    accommodation = models.CharField(max_length=100, null=True, blank=True, verbose_name="Yashash joyi")
    level = models.CharField(max_length=50, null=True, blank=True, verbose_name="Daraja")
    semester = models.CharField(max_length=50, null=True, blank=True, verbose_name="Semestr")
    image = models.URLField(null=True, blank=True, verbose_name="Rasm")

    def __str__(self):
        return self.full_name

class StudentService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Talaba")
    request_type = models.CharField(max_length=200, verbose_name="So‘rov turi", choices=[
        ("schedule", "Dars jadvali"),
        ("retake_application", "Qayta o‘qish uchun ariza"),
        ("exam_list", "Imtihonlar ro‘yxati"),
        ("transcript", "Transkript"),
        ("certificate", "Talaba guvohnomasi"),
        ("gpa_info", "GPA ma’lumotnoma"),
        ("password_reset", "Parolni tiklash"),
        ("medical_insurance", "Tibbiy sug‘urta"),
        ("transfer_application", "O‘qishni ko‘chirish"),
        ("subsidy_application", "Ijara subsidiyasi"),
        ("dorm_application", "Yotoqxonaga ariza"),
    ])
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="So‘rov sanasi")
    status = models.CharField(max_length=50, default="pending", choices=[
        ("pending", "Kutilmoqda"),
        ("in_progress", "Jarayonda"),
        ("completed", "Yakunlangan"),
    ])
    response = models.TextField(null=True, blank=True, verbose_name="Javob")

    def __str__(self):
        return f"{self.student.full_name} - {self.request_type} ({self.id})"

# Akademik qarzdorlik
class AcademicDebt(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Talaba")
    subject = models.CharField(max_length=200, verbose_name="Fan")
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Qarz summasi")
    retake_status = models.CharField(max_length=50, default="pending", choices=[
        ("pending", "Kutilmoqda"),
        ("paid", "To‘langan"),
        ("retaken", "Qayta topshirilgan"),
    ])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    def __str__(self):
        return f"{self.student.full_name} - {self.subject} ({self.id})"

# Ilmiy va innovatsion faoliyat sektori
class ResearchService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Talaba")
    service_type = models.CharField(max_length=200, verbose_name="Xizmat turi", choices=[
        ("grant_info", "Grantlar haqida ma’lumot"),
        ("conference_info", "Ilmiy konferensiyalar"),
        ("startup_registration", "Startap ro‘yxati"),
        ("scholarship_application", "Nomdor stipendiya"),
        ("project_consultation", "Ilmiy loyiha konsultatsiyasi"),
    ])
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="So‘rov sanasi")
    status = models.CharField(max_length=50, default="pending", choices=[
        ("pending", "Kutilmoqda"),
        ("in_progress", "Jarayonda"),
        ("completed", "Yakunlangan"),
    ])
    details = models.TextField(null=True, blank=True, verbose_name="Tafsilotlar")

    def __str__(self):
        return f"{self.student.full_name} - {self.service_type} ({self.id})"

# Xalqaro aloqalar va akademik mobillik sektori
class InternationalService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Talaba")
    service_type = models.CharField(max_length=200, verbose_name="Xizmat turi", choices=[
        ("reference_letter", "Ingliz tilida ma’lumotnoma"),
        ("mobility_program", "Akademik mobillik dasturi"),
        ("visa_service", "Viza xizmatlari"),
        ("foreign_admission", "Xorijda o‘qishga qabul"),
    ])
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="So‘rov sanasi")
    status = models.CharField(max_length=50, default="pending", choices=[
        ("pending", "Kutilmoqda"),
        ("in_progress", "Jarayonda"),
        ("completed", "Yakunlangan"),
    ])
    response = models.TextField(null=True, blank=True, verbose_name="Javob")

    def __str__(self):
        return f"{self.student.full_name} - {self.service_type} ({self.id})"

# Buxgalteriya va marketing sektori
class FinanceService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Talaba")
    service_type = models.CharField(max_length=200, verbose_name="Xizmat turi", choices=[
        ("contract_payment", "To‘lov-shartnoma"),
        ("scholarship_order", "Stipendiya tayinlash"),
        ("retake_payment", "Qayta o‘qish to‘lovi"),
        ("subsidy_application", "Ijara subsidiyasi"),
        ("employment_info", "Ishga joylashish ma’lumotlari"),
    ])
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Summa")
    request_date = models.DateTimeField(auto_now_add=True, verbose_name="So‘rov sanasi")
    status = models.CharField(max_length=50, default="pending", choices=[
        ("pending", "Kutilmoqda"),
        ("in_progress", "Jarayonda"),
        ("completed", "Yakunlangan"),
    ])

    def __str__(self):
        return f"{self.student.full_name} - {self.service_type} ({self.id})"