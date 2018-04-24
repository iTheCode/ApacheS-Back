from rest_framework import serializers
from ApacheS.models import User
 
 
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