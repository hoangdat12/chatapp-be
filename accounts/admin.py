from django.contrib import admin
from .models import Profile, Friend, Post, Comment, Like, Conversation, Message

admin.site.register(Profile)
admin.site.register(Friend)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Conversation)
admin.site.register(Message)
