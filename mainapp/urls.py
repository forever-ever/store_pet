from django.urls import path

from .views import index, blanked_view, bed_set_view, ProductDetailView


urlpatterns = [
    path('', index, name='index'),
    path('products/blanked', blanked_view, name='blanked'),
    path('products/bed-set', bed_set_view, name='bed-set'),
    path('products/<str:ct_model>/<str:slug>', ProductDetailView.as_view(),
         name='product_detail'),
]
