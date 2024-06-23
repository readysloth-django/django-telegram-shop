from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

from django_telegram_bot.models import User
from geoposition.fields import GeopositionField


class Buyer(User):
    real_full_name = models.CharField(_('Full Name'), max_length=128)
    address = models.CharField(_('Address'), max_length=512, null=True)
    position = GeopositionField(_('Geoposition'), default='0,0')

    spendings = models.DecimalField(
        _('Spendings'),
        max_digits=10,
        decimal_places=2,
        default=0
    )
    personal_discount = models.PositiveSmallIntegerField(
        _('Personal discount'),
        null=True,
        validators=[
            MaxValueValidator(100)
        ])

    class Meta:
        verbose_name = _('Buyer')
        verbose_name_plural = _('Buyers')
