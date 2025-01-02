from django.shortcuts import render
from django.http import HttpResponse

from .forms import CreateAccountForm
from .models import Account

# Create your views here.
def home(request):
    return render(request, 'account.html', {'name': 'Henri', 'username': 'tupperwarefan', 'wins': '42', 'losses': '0'})


def render_empty_form(request, error=""):
    form = CreateAccountForm()
    return render(request, 'create_account.html', {"form": form, "error": error})


def create_account(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        
        if form.is_valid():
            account = Account(username=form.cleaned_data["username"], password=form.cleaned_data["password"])

            try:
                account.save()
                return HttpResponse("Success!")
            except:
                return render_empty_form(request, "Username already exists!")
    else:
        return render_empty_form(request)
