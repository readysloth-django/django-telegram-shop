from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from .cart import Cart


class SaleVerificationType(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(_('Name'), max_length=128)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Image'), null=True)

    class Meta:
        verbose_name = _('Sale verification type')
        verbose_name_plural = _('Sale verification types')


class SaleVerification(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    verification_type = models.ForeignKey(
        SaleVerificationType,
        on_delete=models.PROTECT,
        verbose_name=_('Verification type')
    )
    description = models.TextField(_('Description'), null=True)
    file = models.FileField(_('file'), null=True)
    valid = models.BooleanField(_('Valid'), default=False)
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        verbose_name=_('Cart')
    )

    class Meta:
        verbose_name = _('Sale verification')
        verbose_name_plural = _('Sale verifications')

    def __str__(self):
        status = _('Verified')
        return f'{self.cart} {status}'
