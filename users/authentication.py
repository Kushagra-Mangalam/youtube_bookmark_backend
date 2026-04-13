from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class MongoJWTAuthentication(JWTAuthentication):
    """
    Custom JWT authentication that doesn't look up a Django User model.
    Instead it just validates the token and returns the payload.
    This is needed because this project uses MongoDB directly, not Django ORM.
    """

    def get_user(self, validated_token):
        """
        Instead of looking up a Django User, return a simple object
        with the token claims so that request.user works with IsAuthenticated.
        """
        email = validated_token.get("email")
        user_id = validated_token.get("user_id")

        if not email:
            raise InvalidToken("Token contained no recognizable user identification")

        return MongoUser(user_id=user_id, email=email)


class MongoUser:
    """
    A minimal user-like object that satisfies DRF's IsAuthenticated check.
    DRF checks `request.user.is_authenticated` to determine if the user is authenticated.
    """

    def __init__(self, user_id, email):
        self.id = user_id
        self.email = email
        self.is_authenticated = True
        self.is_active = True

    def __str__(self):
        return self.email
