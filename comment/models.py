from django.db import models
from accounts.models import User
from news.models import News


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    status = models.BooleanField(default=True)
