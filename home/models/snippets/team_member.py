from django.db import models

from wagtail.snippets.models import register_snippet

from ..helpers import Person

@register_snippet
class TeamMember(Person):

  title = models.CharField(verbose_name='title', max_lenght=64)
  info = models.TextField(verbose_name='info')

  def __str__(self):
    return f'{self.last_name} {self.first_name}'

  class Meta:
    ordering = ['last_name', 'first_name']

