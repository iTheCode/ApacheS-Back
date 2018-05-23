from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.Users, 'Users')
router.register(r'provider', views.Provider, 'Provider')
router.register(r'typeproducts', views.TypeProducts, 'TypeProducts')
router.register(r'products', views.Products,'Products')
router.register(r'warehouse', views.Warehouse, 'Warehouse')
router.register(r'department', views.Department, 'Department')
router.register(r'province', views.Province, 'Province')
router.register(r'district', views.District, 'District')
router.register(r'company', views.Company, 'Company')
router.register(r'location', views.Location, 'Location')
router.register(r'seller', views.Seller, 'Seller')
router.register(r'purchase', views.Purchase, 'Purchase')
router.register(r'client', views.Client, 'Client')
router.register(r'sale',  views.Sale, 'Sale')
router.register(r'detailSale', views.DetailSale, 'DetailSale')
router.register(r'purcharseDetails', views.PurcharseDetails, 'PurcharseDetails')
api_urlpatterns = router.urls


