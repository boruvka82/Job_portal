from django.urls import path
import jobp.views as views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("teacher/create", views.TeacherCreateView.as_view(), name="teacher_create"),
    path("teacher/list", views.TeacherListView.as_view(), name="teacher_list"),
    path("teacher/update/<int:pk>", views.TeacherUpdateView.as_view(), name="teacher_update"),
    # path("student/create", views.ProfileCreateView.as_view(), name="language_create"),
    # path("student/list", views.ProfileListView.as_view(), name="language_list")
    ]
