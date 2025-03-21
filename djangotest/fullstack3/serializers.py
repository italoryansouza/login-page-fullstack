from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken


#class UserSerializer(serializers.ModelSerializer):
  #  class Meta:
 #       model = User
#        fields = ['id', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True) #write_only=True faz com que a senha não seja incluida nas Responses das APIs
    password2= serializers.CharField(write_only=True) #confirmar a senha

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'as senhas devem ser iguais'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username= data['username'], password= data['password'])
        if not user:
            raise serializers.ValidationError('usuário ou senha incorretos')
            data['user']= User
            return data