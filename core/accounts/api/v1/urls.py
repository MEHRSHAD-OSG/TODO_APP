from django.urls import path, include
from accounts.api.v1 import views

app_name = "accounts_api"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path('api-auth/', include('rest_framework.urls'))

]
