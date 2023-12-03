from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views.generic import ListView

from accounts.forms import LoginForm, SignUpForm, RegisterForm
from accounts.models import User

# Create your views here.

class LoginView(View):
	form_class = LoginForm
	template_name = "accounts/login.html"
	
	def get(self, request):
		form = self.form_class()
		next_url = request.GET.get("next", "")
		nx = next_url
		print(nx)
		return render(request, self.template_name, context={
			"form": form,
			"next": next_url,
		})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				next_url = request.POST.get("next", "")
				if next_url and self.safe_url(next_url):
					return HttpResponseRedirect(next_url)
										
				return HttpResponseRedirect(reverse("blog:index"))
			else:
				message = "Invalid Email or Password."
				return render(request, self.template_name, context={
					"form": self.form_class(),
					"message": message,
				})
			
	def safe_url(self, url):
		return url_has_allowed_host_and_scheme(
			url=url, 
			allowed_hosts=self.request.get_host(), 
			require_https=self.request.is_secure()
		)
			

class ProfileView(LoginRequiredMixin, ListView):
	'''
	CBV que retorna o todos os posts feitos por um usuário.
	context_object_name vai ser o nome do queryset que utilizaremos no template
	{% for post in post_list %} <- post_list é o context_object_name
	'''
	template_name = "accounts/profile.html"
	context_object_name = "post_list"

	def get_queryset(self):
		return self.request.user.owned_posts.all()


class LogoutView(View):
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse("blog:index"))


class SignUpView(View):
	form_class = RegisterForm
	template_name = "accounts/signup.html"

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name, context={
			"form": form
		})
	
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return HttpResponseRedirect(reverse("blog:index"))
		else:
			while (len(form.errors)) != 1:
				form.errors.popitem()
			return render(request, self.template_name, context={
			"form": form
		})

class RegisterView(View):
	form_class = RegisterForm
	template_name = "accounts/register.html"

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name, context={
			"form": form
		})
	
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return HttpResponseRedirect(reverse("blog:index"))
		else:
			return render(request, self.template_name, context={
			"form": form
		})