from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.categoryName


class Products(models.Model):
    productName = models.CharField(max_length=200)
    productPrice = models.IntegerField()
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Authors(models.Model):
    authorName=models.CharField(max_length=200)
    
class Books(models.Model):
    author=models.ManyToManyField(Authors)
    bookName=models.CharField(max_length=200)
    publishedYear=models.DateField()
    
