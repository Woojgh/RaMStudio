from django.shortcuts import render
from shop.models import Cart, Item, Photo, ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView,CreateView, DetailView
from django.views import View
from django.urls import reverse_lazy
from contact.forms import ContactForm


class ShopView(ListView):
    """Render all shop-items."""

    context_object_name = 'shop-items'
    template_name = 'shop.html'
    queryset = Item.objects.all()

    def get_context_data(self):
        context = super(ShopView, self).get_context_data()
        return context


def ShoppingCart(request):
    """Render all cart-items."""

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['flippygonmad@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('success.html')
    return render(request, 'shopping-cart.html', {'form': form})
    # context_object_name = 'cart-items'
    # template_name = 'shopping-cart.html'
    # queryset = Cart.objects.all()
    
    # def shopping_cart_contact_form(request):

    # def get_context_data(self):
    #     context = super(ShoppingCart, self).get_context_data()
    #     return context


class ShopCreateView(LoginRequiredMixin, CreateView):
    """Create a new project and store in the database."""

    template_name = 'item_create.html'
    login_url = reverse_lazy('home')
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('shop')

    def get_form_kwargs(self):
        """Update the kwargs to include the current user's username."""
        kwargs = super(ShopCreateView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        """Assign user as creater of project."""
        form.instance.user = self.request.user
        return super(ShopCreateView, self).form_valid(form)


class ShopDetailView(DetailView):
    """Render the project detail page."""

    template_name = 'item_detail.html'
    model = Item
    pk_url_kwarg = 'id'

    def get_object(self):
        """Get the project object by primary key and check if is public."""
        # import pdb;pdb.set_trace()
        return super(ShopDetailView, self).get_object()
    