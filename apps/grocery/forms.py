from django import forms


class ProductsListSearchForm(forms.Form):
    name = forms.CharField(max_length=150, label='')
