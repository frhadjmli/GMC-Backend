from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


class LogoutAPIView(GenericAPIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"})
