from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.Users, 'Users')

api_urlpatterns = router.urls