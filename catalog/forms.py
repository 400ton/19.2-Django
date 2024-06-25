from django.forms import ModelForm, forms

from catalog.models import Product, Version

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
        exclude = ('created_at', 'updated_at', 'is_published', 'owner')

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(word in name for word in forbidden_words):
            raise forms.ValidationError(f'Cлова {", ".join(forbidden_words)} запрещены')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError(f'Cлова {", ".join(forbidden_words)} запрещены')
            else:
                return description


class VersionForm(ModelForm):
    model = Version
    fields = '__all__'
