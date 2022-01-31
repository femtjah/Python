from django.db import models

from blog.models import Category

# Create your models here.

class CategoryProduct(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoryProd'
        verbose_name_plural='categoriesProd'

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    categories=models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='tienda', null=True, blank=True)
    price=models.FloatField()
    availability=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'