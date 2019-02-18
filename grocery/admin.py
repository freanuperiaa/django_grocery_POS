from django.contrib import admin

from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'category', 'price', 'stocks', 'no_purchases','pub_date']
    list_filter = ['category', 'price', 'pub_date']
    list_editable = ['category', 'price', 'stocks']

admin.site.register(Product)