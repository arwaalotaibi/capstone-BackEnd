from django.urls import path

from .views import isadmin,PostnextQ,UploadImage,ListNextQuestionApiView,CategoryApiView,ListProfileApiView,Postquestion,numberoflikes,userlikes,ListlikesApiView,like,Deletecomment,Postcomment,ListQuestionCommentApiView,UserLoginAPIView ,UserCreateAPIView ,LastQuestionCommentApiView

from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.conf import settings
from api import views

urlpatterns = [
    path('login/',obtain_jwt_token, name='login'),
    path('register/',UserCreateAPIView.as_view(), name='register'),
    path('list/',ListQuestionCommentApiView.as_view(),name='list-api'),
    path('profile/',ListProfileApiView.as_view(),name='list-api'),
    path('next/',ListNextQuestionApiView.as_view(),name='list-api'),
    path('nextQ/',PostnextQ.as_view(),name='list-api'),
    path('last/',LastQuestionCommentApiView.as_view(),name='last-api'),
    path('vote/',like.as_view(),name='last-api'),
    path('isadmin/',isadmin.as_view(),name='isadmin'),
    path('upload/',UploadImage.as_view(),name='upload'),
    path('vote/list',ListlikesApiView.as_view(),name='last-api'),
    path('vote/number',numberoflikes.as_view(),name='vote-api'),
    path('vote/user',userlikes.as_view(),name='user-api'),
    path('comment/',Postcomment.as_view(),name='cc'),
    path('question/',Postquestion.as_view(),name='cc'),
    path('comment/<int:comment_id>/delete/',Deletecomment.as_view(),name='delete-comment'),
    path('category/',CategoryApiView.as_view(),name='category-api'),
   
]
