from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__.meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=9,
                                decimal_places=2)

    def __str__(self):
        return self.title


class BlanketProduct(Product):
    manufacturer = models.CharField(max_length=255,
                                    verbose_name='Производитель')
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return '{}: {}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        get_product_url(self, 'product_detail')


class BedSetProduct(Product):
    manufacturer = models.CharField(max_length=255,
                                    verbose_name='Производитель')
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return '{}: {}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель',
                             on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина',
                             on_delete=models.CASCADE,
                             related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     null=True)
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2,
                                      verbose_name='Общая цена')

    def __str__(self):
        return 'Продукт: {} (для корзины)'.format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец',
                              on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True,
                                      related_name='related_name')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2,
                                      verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    def __str__(self):
        return 'Покупатель: {} {}'.format(self.user.first_name,
                                          self.user.last_name)
