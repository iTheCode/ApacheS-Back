from ApacheS.models import Provider
from ApacheS.models import User
from ApacheS.models import TypeProduct
from ApacheS.models import Product
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
from ApacheS.models import PurcharseDetail
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserSerializer
from .serializers import ProviderSerializer
from .serializers import TypeProductSerializer
from .serializers import ProductSerializer
from .serializers import WarehouseSerializer
from .serializers import DepartmentSerializer
from .serializers import ProvinceSerializer
from .serializers import DistrictSerializer
from .serializers import CompanySerializer
from .serializers import LocationSerializer
from .serializers import SellerSerializer
from .serializers import PurchaseSerializer
from .serializers import ClientSerializer
from .serializers import SaleSerializer
from .serializers import DetailSaleSerializer
from .serializers import PurcharseDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class Users(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class Provider(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer

class TypeProduct(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = TypeProduct.objects.all()
	serializer_class = 	TypeProductSerializer

class Product(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class Warehouse(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Warehouse.objects.all()
	serializer_class = WarehouseSerializer

class Department(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Department.objects.all()
	serializer_class = DepartmentSerializer

class Province(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Province.objects.all()
	serializer_class = ProvinceSerializer

class District(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = District.objects.all()
	serializer_class = DistrictSerializer

class Company(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

class Location(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

class Seller(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

class Purchase(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer

class Client(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class Sale(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

class DetailSale(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = DetailSale.objects.all()
	serializer_class = DetailSaleSerializer

class PurcharseDetail(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = PurcharseDetail.objects.all()
	serializer_class = PurcharseDetailSerializer
