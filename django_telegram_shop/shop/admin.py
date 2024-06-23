from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    Buyer,
    SaleVerificationType,
    SaleVerification,
    Cart,
    ProductCategory,
    Product
)

admin.site.register(Buyer)
admin.site.register(SaleVerificationType)
admin.site.register(SaleVerification)
admin.site.register(Cart)
admin.site.register(ProductCategory)
admin.site.register(Product)
