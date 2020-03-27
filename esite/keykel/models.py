from django.http import HttpResponse
from django.db import models
from django.core.validators import RegexValidator
from wagtail.admin.edit_handlers import FieldPanel

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

class KeyKel(models.Model):
    key_name = models.CharField(primary_key=True, max_length=16)
    key_from = models.DateField(null=True, blank=True)
    key_to = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    panels = [
        FieldPanel('is_active'),
        FieldPanel('key_name'),
        FieldPanel('key_from'),
        FieldPanel('key_to'),
    ]

    def __str__(self):
        return self.key_name