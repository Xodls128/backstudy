from rest_framework import generics
from .serializers import UserSignupSerializer
from django.contrib.auth.models import User

class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    