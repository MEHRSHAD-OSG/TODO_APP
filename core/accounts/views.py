from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserCreationForm, EmailAuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import View

# Create your views here.


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = EmailAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:task_list")


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("todo:task_list")
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("todo:task_list")
        return super().get(request, *args, **kwargs)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("accounts:login")
