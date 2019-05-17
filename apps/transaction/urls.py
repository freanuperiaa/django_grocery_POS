from django.urls import path

from . import views

urlpatterns = [
    path('start/', views.StartTransaction.as_view(), name='start'),
    path('process/<int:id>/', views.TransactionProcessView.as_view(), name='process'),
   ]
