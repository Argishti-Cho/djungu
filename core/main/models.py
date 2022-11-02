# from enum import unique
from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField('Phone Name', max_length=40)
    img = models.ImageField('Phone Image', upload_to='media')
    price = models.IntegerField('Price', blank=True, default=None)
    placeforlink = models.URLField('Add Url')
    description = models.TextField('Description')
    slug = models.SlugField('Phone Slug', unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'


class NoteBook(models.Model):
    name = models.CharField('NoteBook Name', max_length=40)
    img = models.ImageField('NoteBook Image', upload_to='media')
    price = models.IntegerField('Price')
    placeforlink = models.URLField('Add Url')
    description = models.TextField('Description')
    slug = models.SlugField('NoteBook Slug', unique=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NoteBook'
        verbose_name_plural = 'NoteBooks'