from django.contrib import admin

from .models import Category, Product, BlanketProduct, BedSetProduct,\
                    CartProduct, Cart, Customer

admin.site.register(Category)
admin.site.register(BlanketProduct)
admin.site.register(BedSetProduct)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
