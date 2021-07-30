from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quote(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quote')
    body = models.TextField(null=True, blank=True)
    context = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.context
