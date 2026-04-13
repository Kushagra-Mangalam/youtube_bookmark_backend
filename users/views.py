from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import create_user , authenticate_user
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens(user):
    refresh = RefreshToken()
    refresh["user_id"] = str(user.get("_id", ""))
    refresh["email"] = user["email"]
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }

@api_view(["POST"])
def register(request):
    serializer=RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user=create_user(**serializer.validated_data)

        if not user:
            return Response({"error":"User already exists"},status=400)

        token=get_tokens(user)

        return Response({"token":token})
    
    return Response(serializer.errors,status=400)


@api_view(["POST"])
def login(request):
    serializer=LoginSerializer(data=request.data)

    if serializer.is_valid():
        user=authenticate_user(**serializer.validated_data)

        if not user:
            return Response({"error":"Invalid credentials"},status=401)

        token=get_tokens(user)

        return Response({"token":token})
    
    return Response(serializer.errors,status=400)

@api_view(["GET"])
def hello_api(request):
    return Response({"message":"hello from django0"})