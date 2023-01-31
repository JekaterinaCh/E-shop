from django.contrib.auth.hashers import make_password, check_password
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# {
#     "first_name": "John",
#     "last_name": "Doe",
#     "email": "johndoe@example.com",
#     "password": "mysecretpassword",
#     "phone": "1234567890"
# }

# comment.....


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
        user.save()

        return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)

    return Response({"message": "Bad request."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['SESSION_KEY'] = user.pk
                return Response({'status': 'success'})
            else:
                return Response({'status': 'incorrect email or password'})
        except User.DoesNotExist:
            return Response({'status': 'incorrect email or password, user does not exist'})
