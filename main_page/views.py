from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json
import requests
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView

import uuid
import random
import string
import hashlib
import base64
import time

def main_home(request):
    return render(request, 'main_page/main.html')
