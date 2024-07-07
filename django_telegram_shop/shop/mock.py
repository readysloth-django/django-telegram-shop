from datetime import timedelta

from factory.django import (
    DjangoModelFactory,
    FileField
)
from factory import (
    LazyFunction,
    SubFactory,
    lazy_attribute,
)

from mimesis.random import Random
from mimesis import (
    Person,
    Text,
    Datetime,
    Numeric,
    Development,
    Address,
    Food,
    BinaryFile
)

from django_telegram_bot import mock

from .models import (
    Buyer,
    ProductCategory,
    Product,
    Cart,
    SaleVerificationType,
    SaleVerification
)


RANDOM = Random()
PERSON = Person()
DATETIME = Datetime()
TEXT = Text()
NUMERIC = Numeric()
DEVELOPMENT = Development()
ADDRESS = Address()
FOOD = Food()
BINARY_FILE = BinaryFile()


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


class ProductCategoryFactory(DjangoModelFactory):
    class Meta:
        model = ProductCategory

    name = LazyFunction(TEXT.word)
    description = LazyFunction(TEXT.sentence)


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    category = SubFactory(ProductCategoryFactory)
    name = LazyFunction(FOOD.dish)
    description = LazyFunction(FOOD.dish)
    image = FileField(
        data=BINARY_FILE.image(),
        filename='img.png'
    )
    shippable = LazyFunction(DEVELOPMENT.boolean)
    price = LazyFunction(lambda: NUMERIC.decimal_number(start=10, end=1000))
    available = LazyFunction(lambda: NUMERIC.decimal_number(start=0, end=1000))
    discount = LazyFunction(lambda: NUMERIC.decimal_number(start=0, end=20))


class CartFactory(DjangoModelFactory):
    class Meta:
        model = Cart

    buyer = SubFactory(BuyerFactory)
    finished = LazyFunction(DEVELOPMENT.boolean)


class SaleVerificationTypeFactory(DjangoModelFactory):
    class Meta:
        model = SaleVerificationType

    name = LazyFunction(TEXT.word)
    description = LazyFunction(TEXT.sentence)
    image = FileField(
        data=BINARY_FILE.image(),
        filename='img.png'
    )


class SaleVerificationFactory(DjangoModelFactory):
    class Meta:
        model = SaleVerification

    verification_type = SubFactory(SaleVerificationTypeFactory)
    description = LazyFunction(TEXT.sentence)
    file = FileField(
        data=BINARY_FILE.image(),
        filename='img.png'
    )
    valid = LazyFunction(DEVELOPMENT.boolean)
    cart = SubFactory(CartFactory)
