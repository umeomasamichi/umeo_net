from django.db import models
from django.contrib.auth import get_user_model

'''一旦モデル関係あるとこ全部消すぞー！
class Message(models.Model):
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

class Good(models.Model):
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Stock(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Music(models.Model):
    uploader = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    music = models.FileField(upload_to='music/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
'''