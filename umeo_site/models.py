from django.db import models
from django.contrib.auth import get_user_model

class Message(models.Model):
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)