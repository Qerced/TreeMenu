from django.db import models


class Menu(models.Model):
    class Meta:
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

    name = models.CharField(verbose_name='Название меню', max_length=255)
    slug = models.SlugField(
        verbose_name='Адрес меню',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    name = models.CharField(verbose_name='Название элемента', max_length=255)
    category = models.ForeignKey(
        Menu,
        verbose_name='Категория элемента',
        on_delete=models.CASCADE,
    )
    slug = models.CharField(
        verbose_name='Адрес элемента',
        max_length=255,
        unique=True
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский элемент',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
