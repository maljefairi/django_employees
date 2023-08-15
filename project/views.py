from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny

from django.http import HttpRequest


class UserStatus(views.APIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request | HttpRequest, format=None):
        return Response({'is_authenticated': request.user.is_authenticated})
