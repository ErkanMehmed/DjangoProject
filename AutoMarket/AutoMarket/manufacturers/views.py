from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from manufacturers.models import Manufacturer


from manufacturers.forms import ManufacturerCreateForm, ManufacturerUpdateForm


class ManufacturersListView(ListView):
    model = Manufacturer
    template_name = 'manufacturers/list.html'
    context_object_name = 'manufacturers'
    paginate_by = 10

class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'manufacturers/detail.html'

class ManufacturerCreateView(SuccessMessageMixin, CreateView):
    model = Manufacturer
    form_class = ManufacturerCreateForm
    template_name = 'manufacturers/create.html'
    success_url = reverse_lazy('manufacturers-list')
    success_message = 'Manufacturer created successfully'

class ManufacturerUpdateView(SuccessMessageMixin, UpdateView):
    model = Manufacturer
    form_class = ManufacturerUpdateForm
    template_name = 'manufacturers/edit.html'
    success_message = 'Manufacturer updated successfully'

    def get_success_url(self):
        return reverse('manufacturers-detail', kwargs={'pk': self.object.pk})

class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'manufacturers/delete.html'
    success_url = reverse_lazy('manufacturers-list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, f'{self.object.name}: this manufacturer still has vehicles')
            return redirect('manufacturers-detail', pk=self.object.pk)
        messages.success(self.request, 'Successfully deleted manufacturer')
        return response

