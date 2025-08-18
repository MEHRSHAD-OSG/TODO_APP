from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskUpdateForm
from django.views import View
from .models import Task


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    template_name = "todo/list_task.html"
    context_object_name = "tasks"
    model = Task

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("todo:task_list")
    form_class = TaskUpdateForm
    template_name = "todo/update_task.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("This task is not yours")
        return obj


class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        if object.user == request.user:
            object.complete = True
            object.save()
            return redirect(self.success_url)
        raise PermissionDenied("This task is not yours")


class TaskUndo(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        if object.user == request.user:
            object.complete = False
            object.save()
            return redirect(self.success_url)
        raise PermissionDenied("This task is not yours")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task_list")
    template_name = "todo/task_confirm_delete.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied("This task is not yours")
        obj.delete()
        return redirect(self.success_url)
