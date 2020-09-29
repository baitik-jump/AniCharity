from django.db import models

class Tops(models.Model):
    title = models.CharField('Name', max_length=50, default='NoName')
    money = models.IntegerField('money')
    date = models.DateTimeField('Дата доната')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Топ донатов'
        verbose_name_plural = 'Топ донатов'



