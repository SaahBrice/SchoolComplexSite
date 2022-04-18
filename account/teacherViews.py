from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from account.models import CustomUser, Teachers, Classes, Subjects, Students, Academic_years



def teacher(request):
    return render(request, 'teacher/home.html')
