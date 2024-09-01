from django.db import models

# Create your models here.
class Review(models.Model):
    #even though we have validation in form.py we still need to add "max_length=" in "Textfield" here to configure the db correctly
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    #field name can be different in model.py and form.py eg rating, user_name etc
