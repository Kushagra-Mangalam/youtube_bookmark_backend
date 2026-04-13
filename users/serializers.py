from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(
        write_only=True,
        style={'input_type':'password'}
    )

