from django.urls import path
from django.conf.urls.i18n import set_language

from . import views  # Make sure to import views here

urlpatterns = [
    path("login/", views.staff_login, name="staff_login"),
    path("logout/", views.staff_logout, name="staff_logout"),
    path("general/", views.general_exam_page, name="general_exam_page"),
    path('exam_result_view', views.exam_result_view, name='exam_result'),
    path('general/staff_broadsheet/', views.staff_broadsheet, name='staff_broadsheet'),

    # path("login/", views.user_login, name="login"),
    # path('about/', views.about_view, name='about'),  # Ensure the path is registered
    # path("logout/", views.user_logout, name="logout"),


    
    # path('contact/', views.contact, name='contact'),  # Ensure the path is registered
    # path('signup/', views.signup_view, name='signup'),
    # path('register/', views.register, name='register'),





]
