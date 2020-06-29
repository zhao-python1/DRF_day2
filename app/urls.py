from django.urls import path

from app import views

urlpatterns = [

    path("emp/<str:pk>/",views.EmployeeAPIView.as_view()),
    path("emp/", views.EmployeeAPIView.as_view()),
    path("user/<str:pk>/",views.UserAPIView.as_view()),
    path("user/", views.UserAPIView.as_view()),

]