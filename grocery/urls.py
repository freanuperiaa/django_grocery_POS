
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('products/', views.ProductsListView.as_view(), name='products_list'),
    path('products/<slug:slug>/', views.ProductsDetailView.as_view(), name='products_detail'),
    path('addproduct/', views.ProductsCreateView.as_view(), name='create_product'),
    path('products/<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    #

]