from datetime import timedelta

from factory.django import DjangoModelFactory
from factory import (
    LazyFunction,
    SubFactory,
    lazy_attribute
)

from mimesis.random import Random
from mimesis import (
    Person,
    Text,
    Datetime,
    Numeric,
    Development,
    Address
)

from django_telegram_bot import mock

from .models import Buyer


RANDOM = Random()
PERSON = Person()
DATETIME = Datetime()
TEXT = Text()
NUMERIC = Numeric()
DEVELOPMENT = Development()
ADDRESS = Address()


class BuyerFactory(mock.UserFactory):
    class Meta:
        model = Buyer

    address = LazyFunction(ADDRESS.address)
    spendings = LazyFunction(lambda: NUMERIC.decimal_number(start=0, end=10000))
    personal_discount = LazyFunction(
        lambda: NUMERIC.decimal_number(start=0, end=10)
    )

    @lazy_attribute
    def position(self):
        coords = ADDRESS.coordinates()
        lat = coords['latitude']
        lon = coords['longitude']
        return f'{lon},{lat}'
