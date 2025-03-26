from django.urls import path, register_converter
from . import views
from uuid import UUID

class UUIDConverter:
    regex = '[0-9a-f-]{36}'

    def to_python(self, value):
        return UUID(value)

    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('logout/', views.student_logout, name='student_logout'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    # Add similar URLs for other models if needed
    path('student-services/', views.student_service_list, name='student_service_list'),
    path('student-services/create/', views.student_service_create, name='student_service_create'),
    path('student-services/update/<uuid:pk>/', views.student_service_update, name='student_service_update'),

    path('academic-debts/', views.academic_debt_list, name='academic_debt_list'),
    path('academic-debts/create/', views.academic_debt_create, name='academic_debt_create'),
    path('academic-debts/update/<uuid:pk>/', views.academic_debt_update, name='academic_debt_update'),

    path('research-services/', views.research_service_list, name='research_service_list'),
    path('research-services/create/', views.research_service_create, name='research_service_create'),
    path('research-services/update/<uuid:pk>/', views.research_service_update, name='research_service_update'),

    path('international-services/', views.international_service_list, name='international_service_list'),
    path('international-services/create/', views.international_service_create, name='international_service_create'),
    path('international-services/update/<uuid:pk>/', views.international_service_update, name='international_service_update'),

    path('finance-services/', views.finance_service_list, name='finance_service_list'),
    path('finance-services/create/', views.finance_service_create, name='finance_service_create'),
    path('finance-services/update/<uuid:pk>/', views.finance_service_update, name='finance_service_update'),
]

urlpatterns += [
    path('submit-student-service/', views.submit_student_service, name='submit_student_service'),
    path('submit-academic-debt/', views.submit_academic_debt, name='submit_academic_debt'),
    path('submit-research-service/', views.submit_research_service, name='submit_research_service'),
    path('submit-international-service/', views.submit_international_service, name='submit_international_service'),
    path('submit-finance-service/', views.submit_finance_service, name='submit_finance_service'),
]
