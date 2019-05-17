from django.db import models
from django.urls import reverse

from apps.grocery.models import Product, Customer
from django.conf import settings


class Transaction(models.Model):
    served_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'transaction no. {} - {}'.format(self.id, self.date)

    def get_absolute_url(self):
        return reverse('process', args=[self.id])


class TransactionItem(models.Model):
    item = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='transactions')
    quantity = models.PositiveIntegerField(default=1)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE,
                                    related_name='items')

    def __str__(self):
        return self.item.name
