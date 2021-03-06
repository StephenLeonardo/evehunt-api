from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        try:
            request = self.context["request"]
        except KeyError:
            pass

        try:
            request_data = json.loads(request.body)
            if("username" in request_data and "password" in request_data):
                # default scenario in simple-jwt  
                pass

            else:
                # some fields were missing
                raise serializers.ValidationError({"username/otp or username/password" : "These fields are required"})

        except:
            pass
            
            
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',
                'username',
                'email',
                'profile_picture',
                'description',
                'is_verified']
            
            
class AccountPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id',
                'username',
                'email',
                'password',
                'profile_picture',
                'description',
                'is_verified']
                
                
                

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username',
                'email',
                'password',
                'profile_picture',
                'description',]

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email',
                'password']

class RequestVerifSerializer(serializers.Serializer):
    account_id = serializers.CharField()


class LoginReturnSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    class Meta:
        model = Account
        fields = ['id',
                'username',
                'email',
                'profile_picture',
                'description',
                'is_verified',
                'access_token',
                'refresh_token']





    