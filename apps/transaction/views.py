from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from extra_views import FormSetView

from .forms import TransactionItemForm
from .models import Transaction


class StartTransaction(CreateView):
    model = Transaction
    fields = ['customer']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.served_by = self.request.user
        obj.save()
        return redirect(obj.get_absolute_url())


class TransactionProcessView(FormSetView):
    template_name = 'transaction/transactionitem_formset.html'

    def get_formset_class(self):
        this_transaction = Transaction.objects.get(id=self.args[0])
        return TransactionItemForm(initial={'transaction': this_transaction})
