#!/usr/bin/env python

"""
test_crm-products
------------

Tests for `crm-products` models module.
"""

from django.test import TestCase

from tests import factories


class TestModel(TestCase):
    def setUp(self):
        self.catalog = factories.CatalogFactory()
        self.product = factories.ProductFactory()
        self.order = factories.OrderFactory()

    def test_catalog_str(self):
        first_query = self.catalog
        self.assertEqual(first_query.__str__(), first_query.name)

    def test_product_str(self):
        first_query = self.product
        self.assertEqual(first_query.__str__(), first_query.name)

    def test_product_caption(self):
        first_query = self.product
        caption = f"Product name: {first_query.name}\nDescription: {first_query.desc}\nPrice: {first_query.price}\n"
        self.assertEqual(first_query.caption, caption)

    def test_order_str(self):
        first_query = self.order
        self.assertEqual(
            first_query.__str__(),
            f"{first_query.user}: {first_query.product} - {first_query.created}",
        )

    def tearDown(self):
        pass
