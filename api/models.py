from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete= models.CASCADE,related_name="user_questions")
    image=models.ImageField(upload_to="images",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    @property
    def answers(self):
        return self.question_answers.all()
    
    def __str__(self):
        return f'{self.title}'
    
class Answer(models.Model):
    user=models.ForeignKey(User,on_delete= models.CASCADE,related_name="user_answers")
    question=models.ForeignKey(Question,on_delete= models.CASCADE,related_name="question_answers")
    solution=models.TextField()
    votes=models.ManyToManyField(User,related_name="voted_answers")
    created_at=models.DateTimeField(auto_now_add=True) 
    updated_at=models.DateTimeField(auto_now_add=True) 
    
    @property
    def vote_count(self):
        return self.votes.count() 
    
    def __str__(self):
        return f'{self.solution,self.user.username,self.question.title}' 
