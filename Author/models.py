from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")
    username = models.CharField(max_length=50, unique=True, verbose_name="Username")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    action_status = models.BooleanField(default=True, verbose_name="Action Status")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"

class Book(models.Model):

    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=100)  # Choices added here
    status = models.CharField(max_length=100)  # Choices added here


    def __str__(self):
        return self.book_name