from django import forms

max_username_length = 50
max_password_length = 50

class CreateAccountForm(forms.Form):
    username = forms.CharField(label="Username", max_length=max_username_length)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=max_password_length)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=max_username_length) 
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), max_length=max_password_length)
