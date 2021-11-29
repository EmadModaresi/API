from django.db import models
from datetime import datetime


class Book(models.Model):
    author = models.CharField(max_length=150)
    store_name = models.CharField(max_length=50)
    discription = models.TextField()
    image = models.ImageField(default='' ,upload_to='store_book/' , blank=True)
    fav = models.BooleanField()
    create_at = models.DateTimeField(default= datetime.now)

    def __str__(self):
        return self.author
