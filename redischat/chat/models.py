from django.contrib.auth import get_user_model
from django.db import models

class Chat(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body


