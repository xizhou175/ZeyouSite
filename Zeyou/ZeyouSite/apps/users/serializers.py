from rest_framework import serializers
from .models import User, Student, Academy
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings


class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20, min_length=8, write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ("password", "password2", "email", "phone", "username", "department", "token")
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': 'Please enter a eight-twelve digit password',
                    'max_length': 'Please enter a eight-twelve digit password',
                }
            }
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Two passwords are inconsistent')

        # department = data['department']
        # if len(department) < 1 or len(department) > 5:
        #     raise serializers.ValidationError('Wrong department code')
        # for c in department:
        #     if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e':
        #         raise serializers.ValidationError('Wrong department code')

        return data

    def create(self, validated_data):
        print("validated_data",validated_data)
        del validated_data['password2']

        try:
            user = super().create(validated_data)
        except:
            return Response({'message': "用户名已注册", 'status': 201})

        user.set_password(validated_data['password'])
        user.save()

        # 生成JWT

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # 为用户添加token属性
        user.token = token

        return user


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data):
        pass
        #if data["gender"] != 'F' and data["gender"] != 'M':
         #   raise serializers.ValidationError('Gender not correct')

        #if data["identity"] != 0 and data["identity"] != 1:
         #   raise serializers.ValidationError('Identity not correct')

    def create(self, validated_data):
        pass


class AcademySericalizer(serializers.ModelSerializer):
    class Meta:
        model = Academy
