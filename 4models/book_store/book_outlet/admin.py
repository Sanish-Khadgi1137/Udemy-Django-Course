#see https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
from django.contrib import admin

from .models import Book

#we can configure how field are being displayed in the admin form by methode below
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)  #if we have this we do not need blank=True or editable=False in models class Book() here "slug field in models.py"
    #The value of 'readonly_fields' must be a list or tuple. so we added "," to make it tuple

#because of this we do not need over ride method of save() in models.py
    prepopulated_fields = {"slug":("title",)}#for this we need no readonly_fields = ("slug") and there must not be editable=False

    list_filter = ("author", 'rating',)#make filterable by author and rating like in youtube filter by relavance, upload etc
    list_display = ("rating", "title",) #to make colum display with title and rating; order matters

    

# Register your models here.
# admin.site.register(Book)

#to make django aware of admin class here 'BookAdmin'
admin.site.register(Book, BookAdmin)


#we need to make django aware about data that are manage by django admin interface; which can be registered as above; all the models do not need to manage by it eg user generated data