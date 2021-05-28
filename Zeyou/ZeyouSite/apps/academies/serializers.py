from rest_framework import serializers
from .models import Academy
from rest_framework.response import Response
from datetime import date, datetime


class CreateAcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = Academy
        fields = "__all__"

    def validate(self, data):

        return data

    def create(self, validated_data):
        try:
            academy = super().create(validated_data)
            academy.save()
        except:
            return Response({'message': "用户名已注册", 'status': 201})

        return academy
