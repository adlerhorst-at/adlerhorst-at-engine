from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import KeyKel

# Create your user related graphql schemes here.

class KeyKelType(DjangoObjectType):
    class Meta:
        model = KeyKel
        #exclude_fields = ['password']


class Query(graphene.ObjectType):
    keys = graphene.List(KeyKelType)

    def resolve_events(self, info):
        # To list all events
        return KeyKel.objects.all()

