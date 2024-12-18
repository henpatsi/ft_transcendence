from django.shortcuts import render
from django.http import HttpResponse

from datetime import date
from django.db import models

# Create your views here.
def home(request):
    return render(request, 'account.html', {'name': 'Henri', 'username': 'tupperwarefan', 'wins': '42', 'losses': '0'})