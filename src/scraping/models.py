from django.db import models

class city(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название населенного пункта')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Названия населенных пунктов'

    def __str__(self):
        return self.name

class language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Язык программирования')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name
