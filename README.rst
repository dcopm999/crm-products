=============================
crm-products
=============================

.. image:: https://badge.fury.io/py/crm-products.svg
    :target: https://badge.fury.io/py/crm-products

.. image:: https://travis-ci.com/dcopm999/crm-products.svg?branch=master
    :target: https://travis-ci.com/dcopm999/crm-products

.. image:: https://codecov.io/gh/dcopm999/crm-products/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/crm-products

CRM Product App

Documentation
-------------

The full documentation is at https://crm-products.readthedocs.io.

Quickstart
----------

Install crm-products::

    pip install crm-products

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'products.apps.ProductsConfig',
        ...
    )

Add crm-products's URL patterns:

.. code-block:: python

    from products import urls as products_urls


    urlpatterns = [
        ...
        url(r'^', include(products_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
