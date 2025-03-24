from django.db import models

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
