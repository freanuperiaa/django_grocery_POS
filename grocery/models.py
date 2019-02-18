from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30,db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #   return reverse(' {% address of lists of categories %} ', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        'Category',
        on_delete = models.CASCADE,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stocks = models.PositiveIntegerField()
    no_purchases = models.PositiveIntegerField()
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

        
    def get_absolute_url(self):
       return reverse('products_detail', args=[self.slug])
