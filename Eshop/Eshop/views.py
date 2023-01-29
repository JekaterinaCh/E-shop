# enrcyptinti slaptazodzius, paslepti secret key
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        password = request.data['password']
        phone = request.data['phone']

        hashed_password = make_password(password)

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_password,
            phone=phone
        )

        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)

    return Response({"message": "Bad request."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                # Redirect to a success page.
                ...
            else:
                # Return an 'invalid login' error message.
                ...
        except User.DoesNotExist:
            # Return an 'invalid login' error message.
            ...
