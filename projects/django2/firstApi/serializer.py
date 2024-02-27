from rest_framework import serializers

from firstApi.models import UserTable


class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'
