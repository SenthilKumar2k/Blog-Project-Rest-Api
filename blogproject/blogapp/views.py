from .serializers import TagSerializer, CommentSerializer, PostSerializer, UserSerializer, UserLoginSerializer, Replyserializer
from django.contrib.auth.models import User
from .models import Tag, Comment, Post, Reply
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(generics.CreateAPIView):
    quesryset=User.objects.all()
    serializer_class=UserSerializer

    def post(self, request, *args, **kwargs):
        response=super().post(request,*args,**kwargs)
        if response.status_code==status.HTTP_201_CREATED:
            user=User.objects.get(username=request.data['username'])
            refresh=RefreshToken.for_user(user)
            response.data['refresh']=str(refresh)
            response.data['access']=str(refresh.access_token)
        return response
    
class UserLoginView(generics.CreateAPIView):
    serializer_class=UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=User.objects.get(username=serializer.validated_data['username'])
        refresh=RefreshToken.for_user(user)
        return Response({'refresh':str(refresh),'access':str(refresh.access_token)}, status=status.HTTP_200_OK)
    
class UserListView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

class UserEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

class PostListCreateView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

class PostDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

class TagListCreateView(generics.ListCreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer
    permission_classes=[IsAuthenticated]

class TagDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer
    permission_classes=[IsAuthenticated]

class CommentListCreateView(generics.ListCreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated]

class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticated]

class ReplyListCreateView(generics.ListCreateAPIView):
    queryset=Reply.objects.all()
    serializer_class=Replyserializer
    permission_classes=[IsAuthenticated]

class ReplyDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reply.objects.all()
    serializer_class=Replyserializer
    permission_classes=[IsAuthenticated]