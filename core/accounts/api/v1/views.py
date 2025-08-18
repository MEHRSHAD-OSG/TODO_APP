from rest_framework import status, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from accounts.api.v1.serializers import SignUpSerializer,CustomAuthTokenSerializer


class SignUpView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "email": user.email,
            }
        )


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print("=" * 90, request.user.auth_token)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
