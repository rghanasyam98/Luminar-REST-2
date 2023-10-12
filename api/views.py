from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,mixins
from rest_framework import viewsets
from .serializers import UserSerializer,QuestionSerializer,AnswerSerializer
from django.contrib.auth.models import User
from .models import Question,Answer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.decorators import action

# Create your views here.

class UserView(generics.CreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
class QuestionView(viewsets.ModelViewSet):
    serializer_class= QuestionSerializer  
    queryset=Question.objects.all() 
    # used 
    # authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 
        
    # def get_queryset(self):
    #     return Question.objects.exclude(user=self.request.user)  
    
    # http://127.0.0.1:8000/api/question/6/addAnswer/
    @action(methods=["POST"], detail=True)
    def addAnswer(self, request, *args, **kwargs):
        qid = kwargs.get("pk")
        question_object=Question.objects.get(pk=qid)
        
        # question_object=self.get_object()
        answer_serializer=AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
            answer_serializer.save(question=question_object,user=request.user) 
            return Response(data=answer_serializer.data)
        else:
            return Response(answer_serializer.errors) 
               
         
        
class AnswerDeleteView(generics.DestroyAPIView):
    serializer_class = AnswerSerializer
    queryset=Answer.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        return Answer.objects.filter(user=self.request.user)
    
    # @action(methods=["POST"], detail=True)
    # def addvote(self,request,pk):
    #     user=self.request.user
    #     # answer=self.get_object()
    #     answer=Answer.objects.get(pk=pk)
    #     answer.votes.add(user)
    #     return Response(data={"message":"voted successfully"})
        
class AnswerAddVoteView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def create(self, request, pk):
        user = self.request.user
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return Response(data={"message": "Answer not found"}, status=status.HTTP_404_NOT_FOUND)
        
        answer.votes.add(user)
        return Response(data={"message": "Voted successfully"}, status=status.HTTP_201_CREATED) 