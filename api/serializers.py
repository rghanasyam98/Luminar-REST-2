from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question,Answer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},
        }
        
    def create(self, validated_data):
         return User.objects.create_user(**validated_data)
       
       
       
class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    votes = UserSerializer(many=True, read_only=True)
    vote_count=serializers.CharField(read_only=True)
    class Meta:
        model=Answer
        # fields=["title","description","image"]
        fields="__all__"               

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model=Question
        # fields=["title","description","image"]
        fields="__all__"
        
