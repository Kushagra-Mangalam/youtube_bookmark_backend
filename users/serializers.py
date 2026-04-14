from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

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


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    """
    Extends the default refresh serializer to carry over
    the custom 'email' and 'user_id' claims into the new
    access token. Without this, refreshed tokens lack those
    claims and MongoJWTAuthentication rejects them with 401.
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        # Decode the refresh token to read the custom claims
        refresh = RefreshToken(attrs["refresh"])
        email = refresh.get("email", "")
        user_id = refresh.get("user_id", "")

        # Build a new access token that includes the claims
        access = refresh.access_token
        access["email"] = email
        access["user_id"] = user_id

        data["access"] = str(access)
        return data

