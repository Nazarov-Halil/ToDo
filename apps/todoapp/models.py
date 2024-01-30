from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=150,
        verbose_name="Task"
    )
    description = models.TextField(
        verbose_name="Description"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'To-Do'
        verbose_name_plural = 'To'
