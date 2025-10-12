from django.urls import path
from django.conf.urls.i18n import set_language

from . import views  # Make sure to import views here

urlpatterns = [
    path("login/", views.staff_login, name="staff_login"),
    path("logout/", views.staff_logout, name="staff_logout"),
    path("general/", views.general_exam_page, name="general_exam_page"),  # ✅ must match
    path('exam_result_view', views.exam_result_view, name='exam_result'),
    path('general/staff_broadsheet/', views.staff_broadsheet, name='staff_broadsheet'),
    path('about_us/', views.about_us, name='about_us'),
    path('academic_calendar/', views.academic_calendar, name='academic_calendar'),

]
