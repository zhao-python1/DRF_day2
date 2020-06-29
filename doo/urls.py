from django.urls import path

from doo import views

urlpatterns = [
    path("user/",views.user),
    #类视图的定义
    path("users/",views.UserView.as_view()),
    path("users/<str:id>/",views.UserView.as_view()),
    path("usermax/", views.UserAPIView.as_view()),
    path("stu/", views.StudentAPIView.as_view()),
]