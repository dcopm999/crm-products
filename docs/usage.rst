=====
Usage
=====

To use crm-products in a project, add it to your `INSTALLED_APPS`:

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
