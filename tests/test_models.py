#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_crm-products
------------

Tests for `crm-products` models module.
"""

from django.test import TestCase

from products import models


class TestModel(TestCase):
    fixtures = ['products']

    def setUp(self):
        pass

    def test_catalog_str(self):
        first_query = models.Catalog.objects.first()
        self.assertEqual(first_query.__str__(), first_query.name)

    def test_product_str(self):
        first_query = models.Product.objects.first()
        self.assertEqual(first_query.__str__(), first_query.name)

    def test_product_caption(self):
        first_query = models.Product.objects.first()
        caption = f'Product name: {first_query.name}\nDescription: {first_query.desc}\nPrice: {first_query.price}\n'
        self.assertEqual(first_query.caption, caption)

    def test_order_str(self):
        first_query = models.Order.objects.first()
        self.assertEqual(first_query.__str__(), f'{first_query.user}: {first_query.product} - {first_query.created}')

    def tearDown(self):
        pass
