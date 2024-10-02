from django.views.generic import TemplateView, CreateView,ListView
from hotel.models import Post, News
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Welcome(TemplateView):
    template_name = 'welcome.html'


class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactPage(CreateView):
    model = Post
    template_name = 'contact.html'
    fields = ['name', 'email', 'phone_num', 'message']


class NewPost(ListView):
    model = News
    template_name = 'news.html'


class NewsPost(CreateView):
    model = News
    template_name = 'news.html'
    fields = ['news_title', 'news_text', 'news_image']
