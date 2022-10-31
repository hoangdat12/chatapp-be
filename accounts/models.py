from hashlib import blake2b
from venv import create
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, blank=True, default='default.jpg')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True) 
    bio = models.TextField(null= True, blank= True)
    country = models.CharField(max_length=255, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nickname
    
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null= True, blank= True)
    nickname = models.CharField(max_length= 255, null= True, blank= True)
    avatar = models.ImageField(null= True, blank= True)
    avatar_url = models.TextField(null= True, blank= True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nickname


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    status = models.TextField(null = True, blank= True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    active = models.BooleanField(default= True)

    def __str__(self):
        return self.status

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile_comment = models.IntegerField(null= True, blank= True)
    nickname = models.CharField(max_length=255, null= True, blank= True)
    avatar = models.ImageField(null= True, blank= True)
    avatar_url = models.TextField(null= True, blank= True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.content

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userchat = models.IntegerField(null= True, blank= True)
    name = models.CharField(max_length=255, null= True, blank= True)
    nickname = models.CharField(max_length=255)
    avatar = models.ImageField(null= True, blank= True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    userchat = models.IntegerField(null= True, blank= True)
    message = models.TextField(null= True, blank= True)
    my_message = models.TextField(null= True, blank= True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.message or self.my_message
