from django.urls import path
from accounts import views

app_name = "auth"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"), # auth:signup
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("register/", views.RegisterView.as_view(), name="register")
]

