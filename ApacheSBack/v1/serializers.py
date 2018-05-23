from rest_framework import serializers
from ApacheS.models import Provider
from ApacheS.models import User
from ApacheS.models import TypeProducts
from ApacheS.models import Products
from ApacheS.models import Warehouse
from ApacheS.models import Department
from ApacheS.models import Province
from ApacheS.models import District
from ApacheS.models import Company
from ApacheS.models import Location
from ApacheS.models import Seller
from ApacheS.models import Purchase
from ApacheS.models import Client
from ApacheS.models import Sale
from ApacheS.models import DetailSale
from ApacheS.models import PurcharseDetails
 
class UserSerializer(serializers.ModelSerializer):
 
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class ProviderSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Provider.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = Provider
        fields = ('id', 'name', 'company')

class TypeProductsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return TypeProducts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = TypeProducts
        fields = ('id', 'typeproducts')                        

class ProductsSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Products.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = Products
        fields = ('id', 'type_products', 'created', 'product_name', 'description')  

class WarehouseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Warehouse.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = Warehouse
        fields = ('id', 'products', 'created', 'total_quantity')  

class DepartmentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field)) 
        instance.save()
        return instance
    class Meta:
        model = Department
        fields = ('id', 'name_department')       

class ProvinceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Province.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta: 
        model = Province
        fields = ('id', 'department', 'name_province')  

class DistrictSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return District.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = District
        fields = ('id', 'province', 'name_district')

class CompanySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = Company
        fields = ('id', 'ruc', 'name_company')

class LocationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta: 
        model = Location
        fields = ('id', 'company', 'department', 'address')

class SellerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Seller.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta: 
        model = Seller
        fields = ('id', 'location', 'first_name', 'last_name', 'dni', 'phone')

class PurchaseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Purchase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance 
    class Meta:
        model = Purchase
        fields = ('id', 'seller', 'provider', 'department', 'date_order', 'date_delivery', 'amount', 'state','address', 'proof_of_payment')

class ClientSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'dni', 'phone')

class SaleSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Sale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = Sale
        fields = ('id', 'seller', 'client', 'department', 'date_order', 'date_delivery', 'cancellation_date', 'amount', 'state', 'address')

class DetailSaleSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return DetailSale.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = DetailSale
        fields = ('id', 'sale', 'products', 'quantity', 'price', 'discount')

class PurcharseDetailsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return PurcharseDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for field in validated_data:
            instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance
    class Meta:
        model = PurcharseDetails
        fields = ('id', 'purchase', 'products', 'quantity', 'price')