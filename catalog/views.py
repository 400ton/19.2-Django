import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory, ModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, VersionForm, StyleFormsMixin
from catalog.models import Product, Version, Category
from config.services import get_cached_data


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('feedback.txt', 'a') as file:
            file.write(f'{timestamp}, {phone}, {name}: {message}\n')
        return super().get(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')
    login_url = "users:login"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить продукт'
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductModeratorForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'category', 'is_published']


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        return get_cached_data(self.model)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, fields='__all__', extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('catalog.cancellation_of_publication') and user.has_perm('catalog.changes_the_description')
                and user.has_perm('catalog.changes_the_category')):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('cancellation_of_publication') and user.has_perm('changes_the_description')
                and user.has_perm('changes_the_category')):
            return ProductModeratorForm
        raise PermissionDenied


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории продуктов'
        return context

    def get_queryset(self):
        return get_cached_data(self.model)
