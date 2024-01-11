from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag, Post, Comment,Reply

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        extra_kwargs={
            'password':{'write_only':True}
        }

class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=25)
    password=serializers.CharField(max_length=25)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'
        extra_kwargs={
            'tags':{'required':False}
        }

class Replyserializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model=Reply
        fields="__all__"

    def create(self, validated_data):
        validated_data['author']=self.context['request'].user
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    comment=Replyserializer(many=True, read_only=True)
    class Meta:
        model=Comment
        fields='__all__'
        extra_kwargs={
            'comment':{'required':False}
        }

    def create(self, validated_data):
        validated_data['author']=self.context['request'].user
        return super().create(validated_data)

class PostSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True, read_only=True)
    comments=CommentSerializer(many=True,read_only=True)
    author=UserSerializer(read_only=True)

    class Meta:
        model=Post
        fields='__all__'
        extra_kwargs={
            'tags':{'required':False}
        }

    def create(self, validated_data):
        # Set the author field to the current user making the request
        validated_data['author'] = self.context['request'].user
        tags_data=validated_data.pop('tags',[])
        post=super().create(validated_data)
        for tag_data in tags_data:
            tag=Tag.objects.get_or_create(name=tag_data['name'])
            post.tags.add(tag)
        return post
