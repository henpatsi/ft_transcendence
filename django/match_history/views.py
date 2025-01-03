from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.db.models import Q

from .models import Match

# Create your views here.
@login_required
def history(request):
    match_data = Match.objects.filter(Q(winner_id=request.user.id) | Q(loser_id=request.user.id))
    matches = []
    for m in match_data:
        if request.user.id == m.winner_id:
            opponent = User.objects.get(id=m.loser_id).username
            win = "win"
        else:
            opponent = User.objects.get(id=m.winner_id).username
            win = "loss"
        matches.append({"date": m.date, "opponent": opponent, "win": win})
    return render(request, 'history.html', {"matches": matches, "user_id": request.user.id})
