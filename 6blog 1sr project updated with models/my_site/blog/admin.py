from django.contrib import admin

from .models import Author, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "caption", "date",)#the field name should be exactly same as in models.py in "class Post"
    list_display = ("title", "author", "date",)#why to display in admin panel
    prepopulated_fields= {"slug": ("title",)} # to auto populate slug filed with slugified title

admin.site.register(Post, PostAdmin)#we pass PostAdmin here to implement above class
admin.site.register(Author)
admin.site.register(Tag)

#username and password = blog