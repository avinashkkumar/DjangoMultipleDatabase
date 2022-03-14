from django.db import models
from account.models import Account
# Create your models here.

class Post(models.Model):
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)
    name            = models.CharField(max_length=50,null=True)
    text            = models.TextField()
    created_at      = models.DateField(auto_now=False, auto_now_add=True)
    updated_at      = models.DateField(auto_now=True, auto_now_add=False)