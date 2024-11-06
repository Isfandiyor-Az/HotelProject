from django.urls import path

from .views import *

urlpatterns = [
    path('', Welcome.as_view(), name='welcome'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('news/', NewPost.as_view(), name='news'),
]
