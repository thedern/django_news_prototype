from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from hashid_field import HashidAutoField


# Create your models here.
class Article(models.Model):
    """
    Instead of referring to User directly, you should reference the user model using
    django.contrib.auth.get_user_model()
    This method will return the currently active user model – the custom user model if one is specified, or User
    otherwise.
    """
    # hash pk for security
    # id = HashidAutoField(allow_int_lookup=True, primary_key=True)

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    author = models.ForeignKey(
        # get_uer_model ties our active user model to the articles in a single author to many articles relationship.
        # articles is a foreign key to user
        get_user_model(),
        on_delete=models.CASCADE,
    )

    # create a list out of body items
    # def body_as_list(self):
    #     return self.body.split(',')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
