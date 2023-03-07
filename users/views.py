from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated


# Create your views here.


class MyInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data)


from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate, login
from rest_framework import status


# 로그인과 예외 처리
class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            raise ParseError()

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        print(user)

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


from django.contrib.auth import logout


# 서버에서 검사 -> Application -> Cookies ->
class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


# # poetry add pyjwt
# import jwt
# from django.conf import settings


# # settings.py -> SECRET_KEY
# # https://pyjwt.readthedocs.io/en/latest/usage.html
# class JWTLogin(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         if not username or not password:
#             raise ParseError()

#         user = authenticate(
#             request,
#             username=username,
#             password=password,
#         )

#         if user:
#             token = jwt.encode(
#                 {
#                     "id": user.id,
#                     "username": user.username,
#                 },
#                 settings.SECRET_KEY,
#                 algorithm="HS256",
#             )
#             print(token)
#             return Response({"token": token})
