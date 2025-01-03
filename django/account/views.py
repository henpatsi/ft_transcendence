from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateAccountForm, LoginForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, 'account.html', {'name': 'Henri', 'username': 'tupperwarefan', 'wins': '42', 'losses': '0'})


def create_account(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(form.cleaned_data["username"],
                                                form.cleaned_data["email"],
                                                form.cleaned_data["password"])
                return redirect('/account/login')
            except:
                return render(request, 'create_account.html', {"form": form, "error": "Username already exists!"})
    else:
        form = CreateAccountForm()

    return render(request, 'create_account.html', {"form": form, "error": ""})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {"form": form, "error": "Username or password incorrect!"})
    else:
        form = LoginForm()

    return render(request, 'login.html', {"form": form, "error": ""})
