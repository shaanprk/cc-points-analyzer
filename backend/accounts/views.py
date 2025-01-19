from django.shortcuts import render

# Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.conf import settings
# from django.core.mail import send_mail
# from django.core.exceptions import ValidationError
# from .models import User

# class RegisterView(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             # Check if user already exists
#             if User.objects.filter(email=data['email']).exists():
#                 return Response({'error': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)

#             # Create user
#             user = User.objects.create(
#                 username=data['username'],
#                 email=data['email'],
#                 password=make_password(data['password'])
#             )

#             # Send verification email
#             verification_link = f"http://127.0.0.1:8000/accounts/verify/{user.id}/"
#             try:
#                 send_mail (
#                     'Verify your email address',
#                     f'Please verify your email: http://127.0.0.1:8000/accounts/verify/{user.id}/',
#                     settings.DEFAULT_FROM_EMAIL,
#                     [data['email']],
#                     fail_silently=False
#                 )
#             except Exception as email_error:
#                 user.delete()
#                 return Response({'error': 'Failed to send verification email.', 'details': str(email_error)},
#                                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#             return Response({'message': 'Registration successful! Please verify your email.'}, status=status.HTTP_201_CREATED)
#         except ValidationError as ve:
#             return Response({'error': 'Invalid data.', 'details': ve.message_dict}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         # Ensure email and password are provided
#         if not email or not password:
#             return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

#         # Authenticate user
#         user = authenticate(request, username=email, password=password)
#         if user:
#             if not user.is_verified:
#                 return Response({'error': 'Email not verified'}, status=status.HTTP_403_FORBIDDEN)
            
#             # Generate tokens
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'token': str(refresh.access_token),
#                 'refresh': str(refresh)
#             }, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# class VerifyEmailView(APIView):
#     def get(self, request, user_id):
#         try:
#             user = User.objects.get(id=user_id)

#             # Verify email
#             if user.is_verified:
#                 return Response({'message': 'Email already verified'}, status=status.HTTP_200_OK)
            
#             user.is_verified = True
#             user.save()
#             return Response({'message': 'Email verified!'}, status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response({'error': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserRegistrationSerializer, UserLoginSerializer
from .models import User
from django.contrib.auth import authenticate

class RegisterView(APIView):
    """
    Handles user registration
    """
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # Create user
            return Response(
                {'message': 'Registration successful!'}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    """
    Handles user login
    """
    def get(self, request, user_id):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response(
                {'message': 'Login successful!'}, 
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# v1.0
# class RegisterView(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             # Check if the email or username already exists
#             if User.objects.filter(email=data['email']).exists():
#                 return Response({'error': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)
#             if User.objects.filter(username=data['username']).exists():
#                 return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)
            
#             # Create user
#             user = User.objects.create(
#                 username=data['username'],
#                 email=data['email'],
#                 password=make_password(data['password']) # Hash the password
#             )
#             return Response({'message': 'Registration successful!'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'error': 'An error occured during registration.', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginView(APIView):
#     def post(self, request):
#         data = request.data
#         try:
#             # Check if user exists
#             user = User.objects.filter(email=data['email']).first()
#             if not user:
#                 return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
            
#             # Check password
#             if not check_password(data['password'], user.password):
#                 return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
            
#             return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
        
#         # except User.DoesNotExist:
#         #     return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
#         except Exception as e:
#             return Response({'error': 'An error occured during login.', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)