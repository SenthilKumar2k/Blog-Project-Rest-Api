from django.urls import path 
from .views import (UserRegistrationView, UserLoginView, UserListView, UserEditView, 
                    PostListCreateView, PostDetailsView, TagListCreateView, TagDetailsView,
                    CommentListCreateView, CommentDetailsView, ReplyListCreateView, ReplyDetailsView) 

urlpatterns=[
    path('register/',UserRegistrationView.as_view()),
    path('users/',UserListView.as_view()),
    path('user/login/',UserLoginView.as_view()),
    path('user/<int:pk>/',UserEditView.as_view()),
    path('posts/',PostListCreateView.as_view()),
    path('posts/<int:pk>/',PostDetailsView.as_view()),
    path('tags/',TagListCreateView.as_view()),
    path('tags/<int:pk>/',TagDetailsView.as_view()),
    path('comments/',CommentListCreateView.as_view()),
    path('comments/<int:pk>',CommentDetailsView.as_view()),
    path('reply/',ReplyListCreateView.as_view()),
    path('reply/<int:pk>',ReplyDetailsView.as_view()),

]