from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import TemplateView



class HomeView(TemplateView):
    template_name = 'layout.html'

class SignUpSuccess(TemplateView):
    template_name = 'success_register.html'
class SignIn(TemplateView):
    template_name = 'login.html'

