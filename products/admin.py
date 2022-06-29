from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from sorl.thumbnail.admin import AdminImageMixin
from suit.admin import SortableModelAdmin

from products import models


@admin.register(models.Catalog)
class CatalogAdmin(DraggableMPTTAdmin, SortableModelAdmin):
    list_display = ["indented_title"]
    list_display_links = ["indented_title"]
    mptt_level_indent = 20
    sortable = "order"


@admin.register(models.Product)
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ["name", "category", "desc", "image", "price", "is_active"]
    list_filter = ["is_active"]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "created", "is_delivered"]
    list_filter = ["is_delivered"]
    readonly_fields = ["user", "product"]
    list_editable = ["is_delivered"]
    date_hierarchy = "created"
