from django import forms

class ReviewForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=10,error_messages={
        "required:":"Your name must not be empty",
            "max_length":"please enter a shorter name"    })#only works when we removw required fromm default form using inspect in browser
    