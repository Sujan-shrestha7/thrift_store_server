from django.urls import path
from .views import get_teacher, create_teacher, teacher_detail, student_detail, get_student, create_student

urlpatterns =[
    path('school/', get_teacher, name = 'get products'),
    path('school/create/', create_teacher, name = 'create products'),
    path('school/<int:pk>/', teacher_detail, name='product-detail'),
    path('school/student', get_student, name = 'get products'),
    path('school/createstudent/', create_teacher, name = 'create products'),
    path('school/student/<int:pk>/', teacher_detail, name='product-detail'),
]