#for query perfomance use variable for caching which reuse variable and decrease time to visit db
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.urls import reverse

from django.utils.text import slugify

#we use django feature called "models" for database which works in highlevel langugae(python) and it translate django(classes and object) to sql

#see https://docs.djangoproject.com/en/5.0/ref/databases/

#while creating a class for model automatically create incrementing "id" column; i.e. "id = models.AutoField()"(manually)"; which gives unque identifier for every data entry

#this class should extend/inherit from built-in class "models.Model" from django
class Book(models.Model):
    # CharField requires to pass parameter max_length
    title = models.CharField(max_length=50)

    #we do not requires to pass parameter for integerfiled but we can pass
    # rating = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    #in order to make django aware of model/database we need to register app in setting here"book_outlet"
    
    #and we need to tell "django" should reach out to database here "db.sqlite3" with the help of  concept called "migration" which do all the creat/update task related to  database 
    #using python manage.py makemigraions in terminal; staying in project folder here "book_store"; which create migration/create 0001_initial.py file inside migration folder of app here book_outlet
    #to write/update database we run python manage.py migrate; this excute all the migration of all the apps

    #use "python manage.py shell" to use db in terminal shell mode

    # author = models.CharField(max_length=100)
    # is_bestselling = models.BooleanField()
    #when we work on schema or update existing field or add new fields we need to update database too by migration

    #when we already have data in database and we update table or add new flied; we need to look after for new field of old data too, migration create new files 0002_book_au...
    author = models.CharField(null=True, max_length=100)#null=True give null value to empty field but blank is different thing
    is_bestselling = models.BooleanField(default=False)

    #SlugField make whatever string or number stored to slug formate with the help of slugify(); eg "Harry Potter 1" to "harry-potter-1" which is shown to url/link in browser
    # slug=models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)#"db_index=True"(a technical details of databases); add database index for that field; for making find-operation efficient by saving in a that colum which make searching efficient; ID field automatically have database_index, creating database_index for all the field decreases the performance; we made slug db_index because it is frequently used
    slug=models.SlugField(default="",null=False, db_index=True)
    #by default="" and no slug for a dataset; result in error "NoReverseMatch at /" so all the data must have slug i.e. save again for old data
#if editable=False we can't edit this field and do not need to add it when creating data set, or we can use blank=True enable us to keep that field blank yet editable
    #over write built in save() method to auto polulate slug with "title" when we save() the data 
    
    #super() ensures django's built-in save() method still get called in function/method below
    def save(self, *args, **kwargs): #self is used to point on the current object and help in make changes in current object only without affecting other objects of same class
        self.slug= slugify(self.title)
        super().save(*args, **kwargs)
    #despite of this over ride methode we need to add dummy data to slug in new data in django admin but after save it gets auto poputated as mention in above method; solution is making slug blank=True so that we can leave it blank but when save() gets auto populated


    ############33333333333how instances of the class should output in terminal
    def __str__(self):
        return f'{self.title} ({self.rating})'
    #this method also make fomate to show data in django admin panel too
    
    #kill teminal and run again in new terminal "Book.objects.all()"

#way 2 For model specific url 
    def get_absolute_url(self):
        # return reverse("book-detail", args=[self.id] )
        return reverse("book-detail", args=[self.slug] )

