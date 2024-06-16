from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from catalog.forms import StyleFormsMixin

from users.models import User


class UserRegisterForm(StyleFormsMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserProfileForm(StyleFormsMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'num_phone', 'avatar', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
