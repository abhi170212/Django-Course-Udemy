# from django.db import models
# from django.core.validators import MinValueValidator,MaxValueValidator
# from django.urls import reverse
# from django.utils.text import slugify
# # Create your models here.
# class Book(models.Model):
#      title = models.CharField(max_length=50)
#      rating=models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(5)])
#      # id=models.AutoField()  django khud se add kr deta hai
#      author = models.CharField(null=True,max_length=100)
#      is_bestSelling = models.BooleanField(default=True)
#      slug = models.SlugField(default="",null=False)
     
     
#      def save(self,*args,**kwargs):
#           self.slug = slugify(self.title)
#           super().save(*args,**kwargs)
#      def __str__(self):
#           return f"{self.title} and rating is {self.rating}" 
     
#      def get_absolute_url(self):
#           return reverse("book-detail",args=[self.id])




from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    name=models.CharField(max_length=80)
    code = models.CharField(max_length=2)

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.street} {self.postal_code} {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    
    def __full_name__(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.__full_name__()
        

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_bestSelling = models.BooleanField(default=True)
    slug = models.SlugField(unique=True,editable=True, blank=False,db_index=True)  
    published_countries=models.ManyToManyField(Country)

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} and rating is {self.rating}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])  
