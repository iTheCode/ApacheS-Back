from django.contrib import admin
from .models import User
from .models import Provider
from .models import TypeProduct
from .models import Product
from .models import Warehouse
from .models import Department
from .models import Province
from .models import District
from .models import Company
from .models import Location
from .models import Seller
from .models import Purchase
from .models import Client
from .models import Sale
from .models import DetailSale
from .models import PurcharseDetail

admin.site.register(User)
admin.site.register(Provider)
admin.site.register(TypeProduct)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Department)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Seller)
admin.site.register(Purchase)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(DetailSale)
admin.site.register(PurcharseDetail)
# Register your models here.
