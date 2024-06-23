from uuid import uuid4
from django.db import models

from django.utils.translation import gettext_lazy as _

from .buyer import Buyer


class ProductCategory(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(_('Category Name'), max_length=128, unique=True)
    description = models.CharField(_('Description'), max_length=512, null=True)

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(_('Product Name'), max_length=128)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Product Image'), null=True)
    shippable = models.BooleanField(_('Shippable'))

    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    available = models.PositiveIntegerField(_('Available'))
    discount = models.DecimalField(_('Discount'),
                                   max_digits=10,
                                   decimal_places=2,
                                   null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return f'{self.category}: {self.name}'


class Cart(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)

    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Buyer's cart")
        verbose_name_plural = _('Buyers carts')

    def __str__(self):
        is_finished = _('finished') if self.finished else _('not finished')
        return f'{is_finished} {self.Meta.verbose_name} {self.buyer}'
