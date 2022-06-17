import datetime

from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView

from .models import User, UserType, UserLog
# Create your views here.


class UserAPIView(APIView):
    def post(self, request):
        user_email = request.data.get('email')
        password = request.data.get('password')
        hashed_password = make_password(password)
        user_type = UserType.objects.get(name = request.data.get('user_type'))
        new_user = User.objects.create(
            email = user_email,
            password =hashed_password,
            user_type=user_type)
        UserLog.objects.create(
            user = new_user,
            last_login =datetime.datetime.now(),
            last_apply = datetime.datetime.now()
        )
        new_user.save()
        return Response({'message': '회원가입 성공!'})

class LoginAPIView(APIView):
    def post(self, request):
        user_email = request.data.get('email')
        password = request.data.get('password')
        cur_user = authenticate(request, email=user_email, password=password)
        if cur_user:
            login(request, cur_user)
            UserLog.objects.get(user = cur_user).last_login = datetime.datetime.now()
            return Response({"message" : "로그인 성공!"})
        return Response({"error": "아이디와 비밀번호를 확인하세요!"})
