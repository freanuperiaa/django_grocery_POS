from django.db import models
from django.shortcuts import reverse
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=30,db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
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


MEMBERSHIP = (
    ('Plt', 'Platinum'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver'),
)
GENDER = (
        ('M', 'male'),
        ('F', 'female'),
        ('NONB', 'non-binary'),
        ('PNS', 'prefer not to say'),
)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    gender = models.CharField(
        max_length=30,
        blank=True,
        choices=GENDER
    )
    mem_type = models.CharField(max_length=30, choices=MEMBERSHIP)
    trxn_made = models.PositiveIntegerField(default=0)
    mem_date = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.last_name

    def get_absolute_url(self):
        return reverse('customers', args=[])
