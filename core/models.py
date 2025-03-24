from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    faculty = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=200, null=True, blank=True)
    specialty = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.CharField(max_length=20, null=True, blank=True)
    passport_pin = models.CharField(max_length=20, null=True, blank=True)
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    education_form = models.CharField(max_length=50, null=True, blank=True)
    education_type = models.CharField(max_length=50, null=True, blank=True)
    payment_form = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    accommodation = models.CharField(max_length=100, null=True, blank=True)
    level = models.CharField(max_length=50, null=True, blank=True)
    semester = models.CharField(max_length=50, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name
