from rest_framework import serializers 

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'username',
                  'first_name', 'last_name', 'date_joined')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 100, write_only = True
    )
    confirm_password = serializers.CharField(
        max_length = 100, write_only = True
    )
    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'confirm_password')

    def validate(self, attrs):
        print(attrs)
        if len(attrs['password']) != len(attrs['confirm_password']):
            raise serializers.ValidationError({'password':'Пароли не совпадают'})
        elif len(attrs['password']) < 8 and len(attrs['confirm_password']) < 8:
            raise serializers.ValidationError({'password':'Длина пароля меньше 8 символов'})
    
    def create(self, validated_data):
        user = User.objects.all(
            username = validated_data['username'],
            phone = validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
