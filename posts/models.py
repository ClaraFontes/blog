from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()
    publish_date = models.DateField(auto_now=True) # Automaticamente atualiza a data em cada atualização

    def __str__ (self):
        return self.post_title

