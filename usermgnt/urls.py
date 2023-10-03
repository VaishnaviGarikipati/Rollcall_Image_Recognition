from django.urls import path
from . import views

app_name = 'usermgnt'

urlpatterns=[
    path('student', views.StudLogin),
    path('student/get', views.StudAttGet),
    path('admin', views.AdminLogin),
    path('student/login', views.SLoginAction),
    path('admin/login', views.ALoginAction),
    path('admin/logout', views.Alogout),
    path('student/logout', views.Slogout),
    path('rollcall', views.RollCall)
]