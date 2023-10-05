from django.shortcuts import render
from typing import Any
from django import http
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_registration_info = {
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password1'],  # Use 'password1' field
            }

            # Create a new User instance using your custom user manager
            user = User.objects.create_user(
                email=user_registration_info['email'],
                full_name=user_registration_info['full_name'],
                password=user_registration_info['password']
            )

            return redirect('accounts:login')

        return render(request, self.template_name, {'form': form})
    

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/loginvi.html'
    success_url = 'home:home'

    def setup(self, request, *args, **kwargs):
        self.next= request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                if self.next:
                    return redirect(self.next)
                return redirect(self.success_url)
            else:
                messages.error(request, 'email or password is incorrect.')
        return render(request, self.template_name, {'form': form})
		    