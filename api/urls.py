from django.urls import path

from .views import numberoflikes,userlikes,ListlikesApiView,like,Deletecomment,Postcomment,ListQuestionCommentApiView,UserLoginAPIView ,UserCreateAPIView ,LastQuestionCommentApiView

from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.conf import settings
from api import views

urlpatterns = [
    path('login/',obtain_jwt_token, name='login'),
    path('register/',UserCreateAPIView.as_view(), name='register'),
    path('list/',ListQuestionCommentApiView.as_view(),name='list-api'),
    path('last/',LastQuestionCommentApiView.as_view(),name='last-api'),
    path('vote/',like.as_view(),name='last-api'),
    path('vote/list',ListlikesApiView.as_view(),name='last-api'),
    path('vote/number',numberoflikes.as_view(),name='last-api'),
    path('vote/user',userlikes.as_view(),name='last-api'),
    path('comment/',Postcomment.as_view(),name='cc'),
    path('comment/<int:comment_id>/delete/',Deletecomment.as_view(),name='delete-comment'),
   
]
