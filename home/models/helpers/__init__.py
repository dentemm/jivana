from django.db import models

class Person(models.Model):

  last_name = models.CharField(verbose_name='last name', max_lenght=24)
  first_name = models.CharField(verbose_name='first name', max_length=36)

  image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
  )
  
  class Meta:
    ordering = ['last_name', 'first_name']

