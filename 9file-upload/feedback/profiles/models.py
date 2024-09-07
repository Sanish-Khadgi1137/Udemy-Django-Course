from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # #file store in "uploads" folder by forming "images" folder inside it
    # image = models.FileField(upload_to="images") #this file will not be stored in database, becuase its a bad practise, it load db and makes it slow instead file are stored in the hard drive, FileFiled() do = once we save a model with file - it will take file somewhere in a hard-drive on out disk and only store a path to that file in the db/model so that when it need to use that file/display that image it know where to find that file; it does automatically we do not need to move that file manually
    # # "MEDIA_ROOT" setting will automatically taken in to account when file is upload and move because of FileField()

    #using ImageField we do not have to validate filetype now; so django except only images no pdf and doc etc
    image = models.ImageField(upload_to="images")
    #here we get error massage, we need to install a package for dealing with images specifically and analyzing file for being an image and so on
    #run to install package pillow; run this "python -m pip install Pillow"