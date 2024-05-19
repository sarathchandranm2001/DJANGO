from django import forms

class ReviewForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=10,error_messages={
        "required:":"Your name must not be empty",
            "max_length":"please enter a shorter name"    })
    #only works when we removw required fromm default form using inspect in browser

    review_text=forms.CharField(label="Your Feed Back :",widget=forms.Textarea,max_length=200)
    rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)
    

    