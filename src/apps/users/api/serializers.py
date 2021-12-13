from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ User serializer for create and update """
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """ Create a user with encrypted password and return it """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """ Update a user, setting the password correctly and return it """
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserListSerializer(serializers.ModelSerializer):
    """ User serializer for list representation """
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'last_name': instance['last_name'],
            'email': instance.email,
            'is_active': instance['is_active'],
            'is_admin': instance['is_admin'],
        }
