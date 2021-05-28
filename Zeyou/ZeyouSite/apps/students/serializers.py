from rest_framework import serializers
from .models import Student
from rest_framework.response import Response
from datetime import date, datetime


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate(self, data):
        if data["gender"] != 'F' and data["gender"] != 'M':
            raise serializers.ValidationError('Gender not correct')

        if data["identity"] != 0 and data["identity"] != 1:
            raise serializers.ValidationError('Identity not correct')

        return data

    def create(self, validated_data):
        try:
            student = super().create(validated_data)
            student.save()
        except:
            return Response({'message': "用户名已注册", 'status': 201})

        return student
