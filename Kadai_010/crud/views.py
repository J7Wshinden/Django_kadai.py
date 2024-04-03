from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductDetailView(DetailView):
     model = Product