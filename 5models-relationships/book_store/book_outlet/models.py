#https://docs.djangoproject.com/en/5.0/ref/models/relations/
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

#if there are data in db and we make changes to table may encounter error especially for keys like foreignkey  so; do it in empty db

#one-to-one relationshiop; we use OneToOneField()
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5) #eventhough postal_code is combination of numbers but mathmaticall it is not number
    city = models.CharField(max_length=50)

#how to display Address
    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    #in admin panel spelling of "Addresss" is auto plurized so we got wrong spelling;
    #nested class to add meta confuguration to the model; other propertise are treated as field eg. street, city in above
    class Meta:
        verbose_name_plural = 'Addresses'#for how Address model should display

#one-to-many; we use foreignkey() for one to many
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) # no need of related-name for one to one

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

    #we use foreignKey to connect Author and Book class

#many-to-many; A book can be published to many country and a country can publish many books    
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Countries"

    


#putting/defining variable/class behind and calling from front line in IDE may get error; eg putting Coutry-class behild Book-class and calling Coutnry in Book-class

class Book(models.Model):
    
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    # author = models.CharField(null=True, max_length=100)                               #by default if we do not set "related_name" we can use lower-case of class with "_set" here book_set; but we set "booky" for reverse search here from author point of view to search book 
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null=True, related_name= "booky" )#Author is a class; "on_delete = " say what to do when the author of the book is deleted; CASCADE delete the book too when author is deleted; PROTECT do not delete data if the related data is deleted; SET_NULL set the field to null if data here author is deleted in related models
    #this author field does not save/have Author-object (created name of author); but it have the id of that object of Author class
    is_bestselling = models.BooleanField(default=False)
    slug=models.SlugField(default="",null=False, db_index=True)

    publish_countries = models.ManyToManyField(Country)#no on_delete= for many-to-many
    #use add() to add relationship for many-to-many not =

    
    
    
    # def save(self, *args, **kwargs):
    #     self.slug= slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} ({self.rating})'
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug] )
    

    


