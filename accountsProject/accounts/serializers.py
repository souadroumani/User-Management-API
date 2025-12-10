from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'role']

    def validate(self, data):
        """ Validate password confirmation + password strength """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")

        if not any(c.isdigit() for c in data['password']):
            raise serializers.ValidationError("Password must contain a number.")

        if not any(c.isupper() for c in data['password']):
            raise serializers.ValidationError("Password must contain a capital letter.")

        return data

    def create(self, validated_data):
        """ Remove confirm_password before creating user """
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')

        # Create user using Django's built-in method
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")


        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")

        data["user"] = user
        return data




class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_staff']



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'is_staff']
        extra_kwargs = {
            "email": {"required": False},
            "username": {"required": False},
        }

