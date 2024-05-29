from django.core.mail import send_mail

from blog.models import Blog

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView

from pytils.translit import slugify


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    @staticmethod
    def send_notification():
        send_mail(
            subject='Уведомление',
            message='Ваша блог достигл 100 просмотров!',
            from_email="@yandex.ru",
            recipient_list=[],
        )

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.sign_publication += 1
        self.object.save()

        if self.object.sign_publication >= 100:
            self.send_notification()

        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', )
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:list', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
