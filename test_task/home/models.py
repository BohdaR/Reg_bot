from django.contrib.auth.models import User
from django.db import models


class TelegramUser(models.Model):
    user_id = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='unknown')
    site_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
