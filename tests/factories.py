import datetime
from decimal import Decimal
from random import randint

import factory
from slugify import slugify

from products import models


class UserFactory(factory.django.DjangoModelFactory):
    first_name = "Adam"
    last_name = "Johnson"
    username = factory.lazy_attribute(
        lambda o: slugify(o.first_name + "." + o.last_name)
    )
    email = factory.lazy_attribute(lambda o: o.username + "@example.com")

    @factory.lazy_attribute
    def date_joined(self):
        return datetime.datetime.now() - datetime.timedelta(days=randint(5, 50))

    last_login = factory.lazy_attribute(
        lambda o: o.date_joined + datetime.timedelta(days=4)
    )

    class Meta:
        model = "auth.User"
        django_get_or_create = ("username",)


class CatalogFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = models.Catalog
        django_get_or_create = ("name",)


class ProductFactory(factory.django.DjangoModelFactory):
    category = factory.SubFactory(CatalogFactory)
    image = factory.django.ImageField()
    desc = factory.Faker("catch_phrase")
    price = factory.lazy_attribute(lambda o: Decimal(randint(5, 100)))

    class Meta:
        model = models.Product


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = models.Order
