from django import forms

class usersform(forms.Form):
    email=forms.EmailField()  