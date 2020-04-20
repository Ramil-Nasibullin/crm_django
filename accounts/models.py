from django.db import models
from django.contrib.auth.models import User

# Create your models here.

""" Клиент """


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=200, null=True, verbose_name='Имя')
    phone = models.CharField(max_length=200, null=True, verbose_name='Телефон')
    email = models.CharField(max_length=200, null=True, verbose_name='Почта')
    profile_pic = models.ImageField(default='logo.png', null=True, blank=True, verbose_name='Ваше фото')
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиет"
        verbose_name_plural = "Клиеты"


""" Теги """


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


""" Товар """


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'В кафе'),
        ('Out door', 'С собой'),
    )
    name = models.CharField(max_length=200, null=True, verbose_name='Наименование')
    price = models.FloatField(null=True, verbose_name='Стоимость')
    category = models.CharField(max_length=200, null=True, choices=CATEGORY, verbose_name='Категория')
    discription = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание')
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


""" Заказ """
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
