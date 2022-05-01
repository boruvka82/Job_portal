# from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
import jobp.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = "index.html"


class TeacherCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "jobp.add_teacher"
    model = models.Teacher
    template_name = "teacher/teacher_create.html"
    fields = ["name", "language", "level","price", "about_me", "email"]
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."


class TeacherUpdateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "jobp.change_teacher"
    model = models.Teacher
    template_name = "teacher/teacher_update.html"
    fields = ["name", "language", "level", "price", "about_me", "email"]
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."


class TeacherListView(ListView):
    model = models.Teacher
    template_name = "teacher/teacher_list.html"
    fields = ["name", "language", "price",  "level", "about_me", "email"]
    success_url = reverse_lazy("index")
