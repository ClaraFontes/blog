from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()
    bio = models.TextField()