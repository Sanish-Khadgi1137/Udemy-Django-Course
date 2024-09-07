from django import forms

class ProfileForm(forms.Form):
    # user_image = forms.FileField()

    #using image filed after in model
    user_image = forms.ImageField() # now see in developer mode it will only accept image   (  accept="image/*"  )