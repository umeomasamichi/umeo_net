import datetime

from django.db import models
from django.utils import timezone

class Cola(models.Model):
    type_name = models.CharField(max_length=200)
    yammy = models.BooleanField(default=False)
    def __str__(self):
        return self.type_name
    def is_yammy(self):
        return self.yammy