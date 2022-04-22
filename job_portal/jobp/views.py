from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
import jobp.models as models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"


class TeacherCreateView(CreateView):
    model = models.Teacher
    template_name = "teacher/create_teacher.html"
    fields = ["name", "status", "phone_number", "email", "identification_number"]
    success_url = reverse_lazy("index")

class StudentCreateView(CreateView):
    model = models.Student
    template_name = "student/create_student.html"
    fields = ["company", "sales_manager", "description", "status", "value"]
    success_url = reverse_lazy("index")


class TeacherListView(ListView):
    model = models.Teacher
    template_name = "teacher/list_teacher.html"
    success_url = reverse_lazy("index")

class StudentListView(ListView):
    model = models.Student
    template_name = "student/list_student.html"
    success_url = reverse_lazy("index")





