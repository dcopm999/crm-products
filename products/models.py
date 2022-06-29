from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from slugify import slugify
from sorl.thumbnail import ImageField


class Catalog(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    order = models.PositiveIntegerField(verbose_name=_("Order"))
    slug = models.SlugField(editable=False, verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    # It is required to rebuild tree after save, when using order for mptt-tree
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        Catalog.objects.rebuild()

    class MPTTMeta:
        order_insertion_by = ["order"]


class Product(models.Model):
    category = models.ForeignKey(
        Catalog, on_delete=models.SET_NULL, null=True, verbose_name=_("Category")
    )
    image = ImageField(upload_to="product", verbose_name=_("Image"))
    name = models.CharField(max_length=250, verbose_name=_("Product name"))
    desc = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.01, verbose_name=_("Price")
    )
    is_active = models.BooleanField(default=False, verbose_name=("Active"))
    slug = models.SlugField(editable=False, verbose_name=_("Slug"))

    def __str__(self):
        return self.name

    @property
    def caption(self):
        name = _("Product name")
        name = f"{name}: {self.name}\n"
        price = _("Price")
        price = f"{price}: {self.price}\n"
        desc = _("Description")
        desc = f"{desc}: {self.desc}\n"
        return f"{name}{desc}{price}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User")
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("Product")
    )
    is_delivered = models.BooleanField(default=False, verbose_name=_("Delivered"))
    created = models.DateTimeField(auto_now_add=True, editable=False)
    edited = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.user}: {self.product} - {self.created}"
