from datetime import timedelta

from factory import LazyFunction, SubFactory
from factory.django import DjangoModelFactory
from mimesis.random import Random
from mimesis import (Person,
                     Text,
                     Datetime,
                     Numeric,
                     Development)

from django_telegram_bot import mock

from .models import Buyer


RANDOM = Random()
PERSON = Person()
DATETIME = Datetime()
TEXT = Text()
NUMERIC = Numeric()
DEVELOPMENT = Development()


class BuyerFactory(DjangoModelFactory):
    class Meta:
        model = Buyer
