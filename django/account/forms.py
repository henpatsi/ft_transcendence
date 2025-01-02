from django import forms

class CreateAccountForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)
