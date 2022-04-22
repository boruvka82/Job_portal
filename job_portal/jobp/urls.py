from django.urls import path
import jobp.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("teacher/create", views.TeacherCreateView.as_view(), name="teacher_create"),
    path("teacher/list", views.TeacherListView.as_view(), name="teacher_list"),
    path("student/create", views.StudentCreateView.as_view(), name="student_create"),
    path("student/list", views.StudentListView.as_view(), name="student_list")
    ]