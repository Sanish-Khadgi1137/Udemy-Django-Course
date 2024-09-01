#this is similar to model field but this do not effect in database
from django import forms

#  # "Form" in "ReviewForm" is convention of class naming but it is not technically required
#  class ReviewForm(forms.Form):
#     #user_name = forms.CharField()
#     #django uses above field name in pascal case with underscore to white  eg "User name:" to display

#  #customizing field
#  #by default required=True we can make it "False" by mentioning
#     user_name = forms.CharField(label="Your Name:-", max_length=10, error_messages={
# #       "required":"This field can not be empty!",
# #       "max_length":"Please enter a shoter name!"
# #    })

#  #form do not have textfield so we use Charfield and feature widget=forms.Textare
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(min_value=1,max_value=5)

#Modelforms django create a form based on the model like in admin panel
from .models import Review 

class ReviewForm(forms.ModelForm):
    class Meta:
      model=Review
      #fields = ['user_name', 'review_text', 'rating']# added certain fields get used in form from model field eg user_name
      fields = "__all__" #special identifier "__all__" tells django all the fields/property in the model should receives forms which is render expect automaticly added id field 
      #exclude = ["owner_comment"] # to add all except owner_comment

      #configuring form in label with own lable etc using special "labels" key, fields/property name are from the models.py eg "user_name", "review_text" below
      labels = {
          "user_name" : "Your sweet Name",
          "review_text" : "Your sweet Feedback",
          "rating" : "Your sweet Ratin"
          }
      
      error_messages = {
         "user_name":{
                  "required":"This field can not be empty!",
                  "max_length":"Please enter a shoter name!"

         }
      }
