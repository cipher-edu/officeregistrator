from django.urls import path
from .views import *

urlpatterns = [
    path("login/", student_login, name="student_login"),
    path("logout/", student_logout, name="student_logout"),
    path("dashboard/", student_dashboard, name="student_dashboard"),
]
