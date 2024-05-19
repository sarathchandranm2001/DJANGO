from django import forms

class ReviewForm(forms.Form):
    name=forms.CharField()