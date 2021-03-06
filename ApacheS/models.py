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
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dni = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
class TypeProduct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    typeproduct = models.CharField(max_length=50, default='')
class Product(models.Model):
    type_product = models.ForeignKey(TypeProduct, null=False,  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=False)
    product_name = models.CharField(max_length=100, default='', null=False)
    quantity = models.IntegerField(null=False)
    description = models.TextField()
    unit_price_sale = models.FloatField(null=False)
    unit_price_purchase = models.FloatField(null=False)
    igv = models.FloatField()
class Warehouse(models.Model):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
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
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, null=False, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, null=False, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    amount = models.FloatField(null=False)
    state = models.CharField(max_length=25, null=False)
    address = models.TextField(null=False)
    payment_type = models.CharField(max_length=25, null=False)
    number_purchase = models.IntegerField(null=False)
    igv = models.FloatField()
class Client(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dni = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)
class Sale(models.Model):
    seller = models.ForeignKey(Seller, null=False, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, null=False, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=False, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=25, null=False)
    document_type = models.CharField(max_length=25, null=False)
    date = models.DateField(null=False)
    amount = models.FloatField(null=False)
    state = models.CharField(max_length=25, null=False)
    address = models.TextField(null=False)
    number_sale = models.IntegerField(null=False)
    igv = models.FloatField()
class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    discount = models.FloatField()
    igv = models.FloatField()
class PurcharseDetail(models.Model):
    purchase = models.ForeignKey(Purchase, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    igv = models.FloatField()
