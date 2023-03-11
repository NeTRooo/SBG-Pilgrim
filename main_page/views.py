from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
import json
import requests
from allauth.socialaccount.models import SocialAccount


def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    else:
        return render(request, 'main_page/login.html')

def main_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/main.html')
    else:
        return redirect('login_page')

def profile_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/profile.html')
    else:
        return redirect('login_page')

def check_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/check.html')
    else:
        return redirect('login_page')

def applications_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/applications.html')
    else:
        return redirect('login_page')

def help_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/help.html')
    else:
        return redirect('login_page')

def settings_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/settings.html')
    else:
        return redirect('login_page')

def custom_logout(request):
    logout(request)
    return redirect('main_page')

