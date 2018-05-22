from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class User(AbstractUser):
    pass
class Provider(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')
    company = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ('created',)
class TypeProducts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    typeproducts = models.CharField(max_length=50, default='')
class Products(models.Model):
    type_products = models.ForeignKey(TypeProducts, null=False,  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=False)
    product_name = models.CharField(max_length=100, default='', null=False)
    description = models.TextField()
class Warehouse(models.Model):
    products = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    total_quantity = models.IntegerField(null=False)
class Department(models.Model):
    name_department = models.CharField(max_length=100, null=False)
class Province(models.Model):
    department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    name_province = models.CharField(max_length=100, null=False)
class District(models.Model):
    province = models.ForeignKey(Province, null=False, on_delete=models.CASCADE)
    name_district = models.CharField(max_length=100, null=False)
class Company(models.Model):
    ruc = models.IntegerField(null=False)
    name_company = models.CharField(max_length=100, null=False)
class Location(models.Model):
    company = models.ForeignKey(Company, null=False, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    address = models.TextField()
class Seller(models.Model):
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dni = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
class Purchase(models.Model):
    seller = models.ForeignKey(Seller, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, null=False, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    date_order = models.DateField(null=False)
    date_delivery = models.DateField(null=False)
    amount = models.FloatField(null=False)
    state = models.CharField(max_length=25, null=False)
    address = models.TextField(null=False)
    proof_of_payment = models.CharField(max_length=25, null=False)
class Client(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dni = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
class Sale(models.Model):
    seller = models.ForeignKey(Seller, null=False, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    date_order = models.DateField(null=False)
    date_delivery = models.DateField(null=False)
    cancellation_date = models.DateField(null=False)
    amount = models.FloatField(null=False)
    state = models.CharField(max_length=25, null=False)
    address = models.TextField(null=False)
class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, null=False, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    discount = models.FloatField()
class PurcharseDetails(models.Model):
    purchase = models.ForeignKey(Purchase, null=False, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
