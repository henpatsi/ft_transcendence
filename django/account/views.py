from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Henri', 'username': 'tupperwarefan', 'wins': '42', 'losses': '0'})