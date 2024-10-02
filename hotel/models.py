from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=13)
    message = models.TextField()

    def get_absolute_url(self):
        return f'/contact/{self.id}'

    def __str__(self):
        return '{}{}'.format(self.name, self.phone_num)


class News(models.Model):
    news_title = models.CharField(max_length=250)
    news_text = models.CharField(max_length=250)
    news_image = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name = 'New'

    def __str__(self):
        return '{}'.format(self.news_title)
