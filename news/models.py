from django.db import models

from accounts.models import User
from categories.models import Category
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    details = RichTextUploadingField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news')
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
