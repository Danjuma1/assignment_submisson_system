from django.urls import path
from .views import *


app_name = "accounts"

urlpatterns = [
    # Students related urls
    path('student/register', RegisterStudentView.as_view(), name='student-register'),
    path('student/profile/update/', EditStudentProfileView.as_view(), name='student-profile-update'),

    # Lecturer related urls
    path('lecturer/register', RegisterLecturerView.as_view(), name='lecturer-register'),
    path('lecturer/profile/update/', EditLecturerProfileView.as_view(), name='lecturer-profile-update'),

    # login and logout
    path('login', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
