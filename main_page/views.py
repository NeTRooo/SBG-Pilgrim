from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
import json
import requests
from allauth.socialaccount.models import SocialAccount
from .models import UsersStats, UsersLvl, LinkPassword, LinkData
from .forms import OTPForm
import random
import string

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def login_page(request):
    if request.user.is_authenticated:
        return redirect('profile_page')
    else:
        if request.method == 'POST':
            encrypted = random_char(32)
            obj = LinkPassword()
            obj.encrypted = encrypted
            obj.save()
            return redirect(f'https://t.me/SBGPilgrim_Bot?start={encrypted}')
        else:
            return render(request, 'main_page/login.html')

def tgauth(request, encrypted):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            # {"date":"2023-04-10T16:51:00.107Z","name":"DenSSS","team":"RED","xp":899966,"captures":1663,
            # "neutralizes":3410,"cores_deployed":8980,"cores_destroyed":16996,"owned_points":21,"guard_point":10,
            # "lines":202,"max_line":53030,"guard_line":0,"lines_destroyed":1527,"discoveries":3840,"unique_visits":777,"unique_captures":754}
            try:
                enc = LinkPassword.objects.get(encrypted=encrypted)
            except (ValueError, ObjectDoesNotExist):
                return render(request, 'main_page/otp_error.html')
            if type(enc.tgdata) == type(None):
                return render(request, 'main_page/otp_error.html')
            else:
                json_object = json.loads(enc.tgdata)
                print(json_object["id"])
                try:
                    tuser = User.objects.get(email=f'{json_object["id"]}@densss.ru')
                    log_user = authenticate(username=json_object["id"], password=tuser.first_name)
                except (ValueError, ObjectDoesNotExist):
                    user = User.objects.create_user(username=json_object["id"],
                                                    email=f'{json_object["id"]}@densss.ru',
                                                    password=f'{json_object["id"]}asd{json_object["id"]}',
                                                    first_name=f'{json_object["id"]}asd{json_object["id"]}',
                                                    last_name=json_object["id"])
                    user.save()
                    log_user = authenticate(username=json_object["id"], password=f'{json_object["id"]}asd{json_object["id"]}')
                    obj = LinkData()
                    obj.tgdata = enc.tgdata
                    obj.save()
                    obj.user.add(user)
                    obj.save()
                    obj1 = UsersStats()
                    obj1.user_nick = json_object["id"]
                    obj1.total_check = 0
                    obj1.new_accept = 0
                    obj1.new_deny  = 0
                    obj1.new_dubls = 0
                    obj1.update_accept = 0
                    obj1.update_deny = 0
                    obj1.save()
                    obj1.user.add(user)
                    obj1.save()
                    obj2 = UsersLvl()
                    obj2.user_nick = json_object["id"]
                    obj2.lvl = 0
                    obj2.exp = 0
                    obj2.save()
                    obj2.user.add(user)
                    obj2.save()
                if log_user is not None:
                    LinkPassword.objects.filter(encrypted=encrypted).delete()
                    login(request, log_user)
                return redirect('profile_page')
        else:
            form = OTPForm()
            return render(request, 'main_page/otp.html', {"form": form})
    else:
        try:
            enc = LinkPassword.objects.get(encrypted=encrypted)
        except (ValueError, ObjectDoesNotExist):
            return render(request, 'main_page/otp_error.html')
        if type(enc.password) == type(None):
            return render(request, 'main_page/otp_error.html')
        else:
            form = OTPForm()
            return render(request, 'main_page/otp.html', {"form": form})

def main_page(request):
    if request.user.is_authenticated:
        return render(request, 'main_page/main.html')
    else:
        return redirect('login_page')

def profile_page(request):
    if request.user.is_authenticated:
        userstats_db = UsersStats.objects.get(user_nick=request.user.last_name)
        return render(request, 'main_page/profile.html', {"userstats":userstats_db})
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

