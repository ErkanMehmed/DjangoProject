from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from vehicles.forms import VehicleFilterForm, VehicleCreateForm, VehicleUpdateForm, FeatureForm
from vehicles.models import Vehicle, Manufacturer, Feature


class VehicleListView(ListView):
        model =  Vehicle
        template_name = 'vehicles/vehicle_list.html'
        context_object_name = 'vehicles'
        paginate_by = 9

        def get_queryset(self):
            queryset = super().get_queryset().select_related('manufacturer')

            self.filter_form = VehicleFilterForm(self.request.GET)

            if self.filter_form.is_valid():
                data = self.filter_form.cleaned_data

                if data['q']:
                    queryset = queryset.filter(model_name__icontains=data['q'])
                if data['manufacturers']:
                    queryset = queryset.filter(manufacturer=data['manufacturers'])
                if data['max_price']:
                    queryset = queryset.filter(price__lte=data['max_price'])
                if data['sort']:
                    queryset = queryset.order_by(data['sort'])

            return queryset

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['filter_form'] = self.filter_form
            return context

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicles/vehicle_detail.html'

    def get_queryset(self):
        return (super().get_queryset().select_related('manufacturer'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['similar_vehicle'] = (Vehicle.objects.filter(manufacturer=self.object.manufacturer)).exclude(pk=self.object.pk)[:3]
        return context

class VehicleCreateView(SuccessMessageMixin, CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    template_name = 'vehicles/vehicle_create.html'
    success_message = "Vehicle created successfully"

    def get_success_url(self):
        return reverse('vehicle-detail', kwargs={'pk': self.object.pk})

class VehicleUpdateView(SuccessMessageMixin, UpdateView):
    model = Vehicle
    form_class = VehicleUpdateForm
    template_name = 'vehicles/vehicle-edit.html'
    success_message = "Vehicle updated successfully"

    def get_success_url(self):
        return reverse('vehicle-detail', kwargs={'pk': self.object.pk})

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicles/vehicle_delete.html'
    success_url = reverse_lazy('vehicle-list')

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, 'Successfully deleted vehicle')
        return redirect('vehicle-list')

class FeatureListView(ListView):
    model = Feature
    template_name = 'vehicles/feature_list.html'
    context_object_name = 'features'
    paginate_by = 20

class FeatureCreateView(SuccessMessageMixin, CreateView):
    model = Feature
    form_class = FeatureForm
    template_name = 'vehicles/feature_create.html'
    success_url = reverse_lazy('feature-list')
    success_message = 'Feature created successfully'