from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption=models.CharField(max_length=10)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):#this also comes into effect in html file and show full name
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)

    # this is not image; we can see it in "File Upload section"
    image_name = models.CharField(max_length=100)

    # auto_now=True means update date every time post gets update
    date = models.DateField(auto_now=True)# see django datefield

    # "unique=True" make it unique like id; "db_index=True" make quering effective; we do not need it here as we have unique=true and slugfield automatically have "db_index=True" see documentation
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    # SET_NULL means set author field null if author is deleted post
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    #we need to set null=True i.e. to allow null value for field for "on_delete=models.SET_NULL"

    caption = models.ManyToManyField(Tag)
