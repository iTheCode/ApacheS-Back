from ApacheS.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

 
class Users(viewsets.ModelViewSet):
	authentication_class = (JSONWebTokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer