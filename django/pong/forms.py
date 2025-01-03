from django import forms

class TestPongForm(forms.Form):
    winner = forms.IntegerField(label="Winner")
    loser = forms.IntegerField(label="Loser")
