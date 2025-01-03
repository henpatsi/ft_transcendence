from django.shortcuts import render
from django.http import HttpResponse

from .forms import TestPongForm

from match_history.models import Match
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def pong(request):
    if request.method == "POST":
        form = TestPongForm(request.POST)
        if form.is_valid():
            try:
                winner_id = int(form.cleaned_data["winner"])
                loser_id = int(form.cleaned_data["loser"])
                match = Match(winner=User.objects.get(id=winner_id), loser=User.objects.get(id=loser_id))
                match.save()
                return HttpResponse("Match complete!")
            except:
                return render(request, 'pong.html', {"form": form, "error": "User does not exist!"})
    else:
        form = TestPongForm()

    return render(request, 'pong.html', {'form': form, 'error': ""})

