from django.urls import path
from .views import *

urlpatterns = [
    path("login/", student_login, name="student_login"),
    path("dashboard/", student_dashboard, name="student_dashboard"),
]
