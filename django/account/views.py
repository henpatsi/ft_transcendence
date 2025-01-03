from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateAccountForm, LoginForm

from match_history.models import Match

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def account(request):
    name = request.user.username
    wins = Match.objects.filter(winner_id=request.user.id).count()
    losses = Match.objects.filter(loser_id=request.user.id).count()
    return render(request, 'account.html', {'username': name, 'wins': wins, 'losses': losses})


def create_account(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(form.cleaned_data["username"],
                                                form.cleaned_data["email"],
                                                form.cleaned_data["password"])
                return redirect('/accounts/login/')
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


def logout_user(request):
    logout(request)
    return redirect('/')
