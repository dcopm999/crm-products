# -*- coding: utf-8 -*-
from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from sorl.thumbnail.admin import AdminImageMixin

from products import models


@admin.register(models.Catalog)
class CatalogAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'name', 'parent']
    list_display_links = ['name']
    mptt_level_indent = 20
    

@admin.register(models.Product)
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['name', 'category', 'desc', 'image', 'price', 'is_active']
    list_filter = ['is_active']


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created', 'is_delivered']
    list_filter = ['is_delivered']
    readonly_fields = ['user', 'product']
    list_editable = ['is_delivered']
    date_hierarchy = 'created'
