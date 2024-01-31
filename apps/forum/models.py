from django.db import models

# Create your models here.
class Forum(models.Model):
    title = models.TextField(
        verbose_name = "Заголовок"
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    created = models.DateTimeField(
        
    )