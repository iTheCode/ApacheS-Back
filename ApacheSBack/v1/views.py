from ApacheS.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserSerializer
 
 
class Users(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer