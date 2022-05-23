from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from core.user.models import User
from core.user.serializers import UserSerializer

class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class RefreshDataViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        email_user = request.user
        user = User.objects.filter(email=email_user).first()
        
        serializer = self.serializer_class(user)
        
        # serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
        