import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.set_password(user.password)
        verification_code = secrets.token_hex(16)
        user.verification_code = verification_code
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email.confirm/{verification_code}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        user.save()
        return super().form_valid(form)


def email_confirm(request):
    verification_code = request.POST.get('verification_code')
    user = get_object_or_404(User, verification_code)
    if user:
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('users:login'))
    else:
        return redirect(reverse_lazy('users:register'))


class ResetPassword(TemplateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def get_template_names(self):
        return 'users/reset_password.html'

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if user:
                password = User.objects.make_random_password(length=8)
                user.set_password(password)
                user.save()
                send_mail(
                    'Смена пароля',
                    f'Ваш новый пароль: {password}',
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                )
            return redirect(reverse("users:login"))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
