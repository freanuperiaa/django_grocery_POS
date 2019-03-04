from django.shortcuts import render,get_object_or_404,redirect
from django.template.defaultfilters import slugify
from django.utils import timezone

from .models import Product,Category, Customer

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.base import View
# Create your views here.


class HomePageView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        query_set = Product.objects.order_by('-no_purchases')[:5]

        return query_set

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = timezone.now()
        
        return context

class ProductsListView(ListView):
    template_name = "products_list.html"
    
    def get_queryset(self):
        query_set = Product.objects.order_by('name')
        return query_set

class ProductsDetailView(View):
    
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Product, slug = kwargs['slug'])
        context = {
            'item' : item,
        }

        return render(request, 'product_detail.html', context)


class ProductsCreateView(CreateView):
    template_name = 'create_product.html'
    model = Product
    fields = [
        'name',
        'category',
        'price',
        'stocks',
        'no_purchases',
        'description',
    ]

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.pub_date = timezone.now()
        obj.slug = slugify(obj.name)
        obj.save()
        return redirect(obj.get_absolute_url())

class ProductUpdateView(UpdateView):
    template_name = 'update_product.html'
    model = Product
    fields = [
        'category',
        'price',
        'stocks',
        'description',
    ]

class CustomersListView(ListView):
    template_name = 'customers_list.html'
    
    def get_queryset(self):
        query_set = Customer.objects.order_by('first_name')
        return query_set

class CustomersCreateView(CreateView):
    template_name = 'create_customer.html'
    model = Customer
    fields = [
        'first_name', 'last_name',
        'gender', 'address',
        'trxn_made', 'mem_type'
    ]


    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.mem_date = timezone.now()
        obj.save()
        return redirect('customers')

class CustomersUpdateView(UpdateView):
    template_name = 'customer_update.html'
    model = Customer
    fields = [
        'first_name', 'last_name',
        'gender', 'address', 'mem_type',
    ]