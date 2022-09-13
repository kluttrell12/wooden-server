from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from woodenapi.models.builder import Builder

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    Handles user authentication

    Args:
        request -- full HTTP request object
    """
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        # build data dictionary to store information to be sent to client side
        data = {
            'valid': True,
            'token': token.key,
            'user_id': authenticated_user.id,
            'is_staff': authenticated_user.is_staff
        }
    else:
        data = { 'valid': False}
    return Response(data)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Handles the creation of new builder for authentication

    Args:
        request -- full HTTP request object
    """
    # set base data for new builders to the application

    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email']
    )

    builder = Builder.objects.create(
        bio=request.data['bio'],
        user=new_user
    )

    token = Token.objects.create(user=builder.user)

    data = {
        'token': token.key,
        'user_id': new_user.id,
        'valid': True,
        'is_staff': new_user.is_staff
    }
    return Response(data, status=status.HTTP_201_CREATED)