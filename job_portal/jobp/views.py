# from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
import jobp.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class IndexView(TemplateView):
    template_name = "index.html"


class TeacherCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = models.Teacher
    template_name = "teacher/teacher_create.html"
    fields = ["name", "language1", "language2", "level", "about_me", "email"]
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."


class TeacherListView(ListView):
    model = models.Teacher
    template_name = "teacher/teacher_list.html"
    fields = ["name", "language1", "language2", "level", "about_me", "location", "contact"]
    success_url = reverse_lazy("index")
