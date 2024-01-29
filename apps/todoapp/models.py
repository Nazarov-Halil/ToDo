from django.db import models
from django.forms import CharField


class ToDo(models.Model):
    title = models.CharField(
        max_length=150,
    )
    description = models.TextField(
        max_length=300
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'To-Do'
        verbose_name_plural = 'To'
