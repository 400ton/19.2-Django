from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории", )
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта", **NULLABLE)
    preview = models.ImageField(upload_to="products/", verbose_name="Фото продукта", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="Категория", related_name="Products",
                                 **NULLABLE)
    price = models.IntegerField(verbose_name="Цена продукта", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", **NULLABLE)
    updated_at = models.DateField(verbose_name="Дата изменения", **NULLABLE)

    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.SET_NULL, **NULLABLE)
    is_published = models.BooleanField(verbose_name="Публикация", default=True, **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description} {self.preview} {self.category} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Продукт", **NULLABLE)
    number = models.PositiveIntegerField(verbose_name="Номер версии продукта")
    name = models.CharField(max_length=150, verbose_name="Название версии")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
