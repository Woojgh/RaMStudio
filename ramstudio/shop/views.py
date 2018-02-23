from django.shortcuts import render
from shop.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView,CreateView, DetailView
from django.views import View
from django.urls import reverse_lazy


class ShopView(ListView):
    """This is the view for the sales page."""

    context_object_name = 'shop-items'
    template_name = 'shop.html'
    queryset = Item.objects.all()

    def get_context_data(self):
        context = super(ShopView, self).get_context_data()
        return context