from django import forms
from django.forms import modelformset_factory

from apps.grocery.models import Product
from .models import TransactionItem, Transaction


class TransactionItemForm(forms.ModelForm):

    item = forms.ModelChoiceField(
        queryset=Product.objects.all(),
    )
    quantity = forms.IntegerField()
    transaction = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=Transaction.objects.all(),
        disabled=True
    )

    class Meta:
        model = TransactionItem
        fields = ('item', 'quantity', 'transaction')


TransactionItemFormSet = modelformset_factory(TransactionItem,
                                              form=TransactionItemForm)
