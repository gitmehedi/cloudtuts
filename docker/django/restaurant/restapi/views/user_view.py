from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from restapi.serializers.user_serializer import UserSerializer


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
