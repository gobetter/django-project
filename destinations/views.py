from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView,
        )

from .forms import DestinationModelForm
from .models import Destination

class DestinationCreateView(CreateView):
    template_name = 'destinations/destination_create.html'
    form_class = DestinationModelForm
    queryset = Destination.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('destinations:destination-list')

    # def get_success_url(self):
    #     return '/'

class DestinationListView(ListView):
    template_name = 'destinations/destination_list.html'
    queryset = Destination.objects.all() # <destinations>/<modelname>_list.html

class DestinationDetailView(DetailView):
    template_name = 'destinations/destination_detail.html'
    # queryset = Destination.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Destination, id=id_)

class DestinationUpdateView(UpdateView):
    template_name = 'destinations/destination_create.html'
    form_class = DestinationModelForm
    # queryset = Destination.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Destination, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'

class DestinationDeleteView(DeleteView):
    template_name = 'destinations/destination_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Destination, id=id_)

    def get_success_url(self):
        return reverse('destinations:destination-list')
