
from django import forms

from .models import Review 

class ReviewForm(forms.ModelForm):
    class Meta:
      model=Review
      fields = "__all__"

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
