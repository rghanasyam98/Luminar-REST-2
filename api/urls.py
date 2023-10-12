from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken


router=DefaultRouter()
router.register('question',views.QuestionView,basename='question')
# router.register('answer',views.AnswerCreateView,basename='answer')

urlpatterns = [
    path("user/", views.UserView.as_view(), name="user"),
    path('token/', ObtainAuthToken.as_view(), name='token_obtain'),
    path('answer/<int:pk>', views.AnswerDeleteView.as_view(), name='answer'),
     path('answer/<int:pk>/addvote', views.AnswerDeleteView.as_view(), name='answer-vote'),
    path('answer/<int:pk>/vote', views.AnswerAddVoteView.as_view(), name='vote'),
    


    
]+router.urls
