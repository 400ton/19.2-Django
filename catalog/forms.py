from django.forms import ModelForm, forms

from catalog.models import Product

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                   'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormsMixin, ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        clean_data = self.cleaned_data.get['name']
        if clean_data in forbidden_words:
            raise forms.ValidationError(f'Cлова {forbidden_words} запрещены')
        else:
            return clean_data

    def clean_product_description(self):
        clean_data = self.cleaned_data.get['description']
        if clean_data in forbidden_words:
            raise forms.ValidationError(f'Cлова {forbidden_words} запрещены')
        else:
            return clean_data

