from django.forms import ModelChoiceField
from django.contrib import admin

from .models import Category, Product, BlanketProduct, BedSetProduct,\
                    CartProduct, Cart, Customer


class BlankedAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='blanked'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BedSetAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bed-set'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(BlanketProduct, BlankedAdmin)
admin.site.register(BedSetProduct, BedSetAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
