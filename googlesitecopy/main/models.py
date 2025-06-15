from django.db import models


class Register(models.Model):
    title = models.CharField('Назва', max_length=20)
    task = models.TextField('Опис')

    def __str__(self):
        return self.title
