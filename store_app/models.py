from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    iin = models.CharField(max_length=12, validators=[MinLengthValidator(12)])

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return str(self.name)


class Good(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)


class Plant(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)