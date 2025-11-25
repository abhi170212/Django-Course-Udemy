from django.db import models
from django.core.validators import MinLengthValidator
#=========
#MODALS 
#==========
class Tag(models.Model):
     caption = models.CharField(max_length=20)
     def tag_name(self):
          return f"{self.caption}"
     def __str__(self):
          return self.tag_name()
     
class Author(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email_address = models.EmailField()
     
     def full_name(self):
          return f"{self.first_name} {self.last_name}"
     
     def __str__(self):
          return self.full_name();
     
class Post(models.Model):
     title = models.CharField(max_length=150)
     excerpt = models.CharField(max_length=300)
     date = models.DateField(auto_now=True)
     slug = models.SlugField(unique=True,db_index=True)
     content=models.TextField(validators=[MinLengthValidator(20)])
     author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL,related_name="posts")
     tags=models.ManyToManyField(Tag)
     image = models.ImageField(upload_to="posts",null=True)
     
     
class Comment(models.Model):
     user_name = models.CharField(max_length=120)
     user_email = models.EmailField()
     text = models.TextField(max_length=400)
     posts = models.ForeignKey(Post,on_delete=models.CASCADE, related_name = "comments")
     
     