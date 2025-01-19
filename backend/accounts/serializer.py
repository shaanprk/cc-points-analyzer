from rest_framework import serializers
from .models import User # Import the User model from the same directory
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
    
    def validate_email(self, email):
        """
        Normalize and validate emails to be case-insensitive
        and account for salting techniques
        """
        email = email.strip().lower()

        # Normalize Gmail-style emails to ignore periods (salting)
        if '@gmail.com' in email:
            local_part, domain = email.split('@')
            local_part = local_part.replace('.', '') # Remove periods from local part
            email = f'{local_part}@{domain}'

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already registered.')
        return email
    
    def validate_username(self, username):
        """
        Normalize and validate usernames to be case-insensitive
        """
        username = username.strip().lower()

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already taken.')
        return username

    def validate(self, data):
        """
        Perform additional validation on the entire input data
        """
        data['email'] = self.validate_email(data['email'])
        data['username'] = self.validate_username(data['username'])
        return data

    def create(self, validated_data):
        """
        Create a new user with a hashed password and normalized email/username
        """
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    def validate(self, data):
        """
        Check if the user exists and the password is correct
        """
        email = data['email'].strip().lower()
        password = data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError({'error': 'Invalid credentials.'})
        return user