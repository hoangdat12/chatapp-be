from decimal import ConversionSyntax
import profile
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Profile, Friend, Post, Comment, Message, Conversation, Like

from .serializers import ProfileSerializer, FriendSerializer, PostSerializer, CommentSerializer, MessageSerializer, ConversationSerializer, LikeSerializer

# Profile 
class ProfileMixinView(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    queryset = Profile.objects.filter()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        return qs.filter(user= self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class SearchProfileView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nickname']
    search_fields = ['nickname']

class ProfileMixinViewGetById(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Profile.objects.filter()
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

@api_view(['GET'])
def get_profile_by_userId(request, pk):
    if not pk:
       return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    if Profile.objects.filter(id=pk).exists():
        profile = Profile.objects.get(user=pk)
        profile = ProfileSerializer(profile)
        return Response(profile.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Profile not found'}, status=status.HTTP_400_BAD_REQUEST)

# Friend
class FriendMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Friend.objects.filter()
    serializer_class = FriendSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return self.list(request, *args, **kwargs)
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class FriendMixinViewByUserId(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Friend.objects.filter()
    serializer_class = FriendSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@api_view(['POST'])
def check_is_friend(request, pk):
    if not pk:
        return Response({'message': 'User Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    if Friend.objects.filter(user= pk ,profile= request.data['profile_id']).exists():
        return Response({'is_friend': True}, status=status.HTTP_200_OK)
    else:
        return Response({'is_friend': False}, status=status.HTTP_200_OK)


# Post
class PostMixinView(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Post.objects.filter()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ListPostUserMixinView(
    mixins.ListModelMixin, 
    generics.GenericAPIView
):
    queryset = Post.objects.filter()
    serializer_class = PostSerializer

    def get_queryset(self) :
        qs = super().get_queryset() 
        return qs.filter(user=self.kwargs['pk']).order_by('-created')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ListPostMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
 

# Comment
class CommentMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommentMixinViewGetByUSerId(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(post = self.kwargs['pk']).order_by('created')
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Conversation
class ConversationMixinView(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Conversation.objects.filter()
    serializer_class = ConversationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConversationMixinViewGetByUserId(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Conversation.objects.filter()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user= self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Message
class MessageView(APIView):
    def post(self, request, pk, format= None):
        message1 = MessageSerializer(data= request.data)
        conversation = Conversation.objects.get(user= request.data['userchat'], userchat= request.data['user'])
        conversation = ConversationSerializer(conversation)
        dataMessage2 = {
            'user': request.data['userchat'],
            'userchat': request.data['user'],
            'conversation': conversation.data['id'],
            'message': request.data['my_message'],
            'my_message': request.data['message']
        }
        message2 = MessageSerializer(data= dataMessage2)
        if message1.is_valid() and message2.is_valid():
            message1.save()
            message2.save()
            return Response({'data': {'message1':message1.data, 'message2':message2.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Create Message is failure'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk, format= None):
        if not pk:
            return Response({'message': 'ID is require'}, status=status.HTTP_400_BAD_REQUEST)
        if Message.objects.filter(id= pk).exists():
            message = Message.objects.get(id= pk)
            message = MessageSerializer(message, data= request.data)
            if message.is_valid():
                message.save()
                return Response({'data': message.data}, status=status.HTTP_200_OK)
            else: 
                return Response({'message': 'Form Data is not valid'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'message not found'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format= None):
        if not pk:
            return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
        if Message.objects.filter(id= pk).exists():
            message = Message.objects.get(id= pk)
            message.delete()

            return Response({'detail': 'Deleted Message is successful'})
        else:
            return Response({'message': 'message not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_all_message(request, pk):
    if not pk:
        return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    messages = Message.objects.filter(user= pk, conversation=request.data['conversation']).order_by('created')
    messages = MessageSerializer(messages, many= True)
    return Response({'data': messages.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_new_message(request, pk):  #Rename function
    if not pk:
        return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    messages = Message.objects.filter(user= pk).order_by('-created')
    messages = MessageSerializer(messages, many=True)
    return Response(messages.data[0], status=status.HTTP_200_OK)

# Like
class CreateLikeMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = LikeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
@api_view(['GET'])
def count_numbers_like(request, pk):
    if not pk:
        return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    if Post.objects.filter(id=pk).exists():
        likes = Like.objects.filter(post=pk).count()
        return Response(likes, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'post not found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def check_user_is_liked(request, pk):
    if not pk:
        return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    if Like.objects.filter(user= request.data['user'], post=pk):
        return Response(True, status=status.HTTP_200_OK)
    else:
        return Response(False, status=status.HTTP_200_OK)

@api_view(['POST'])
def remove_like_post(request, pk):
    if not pk:
        return Response({'message': 'Id is require'}, status=status.HTTP_400_BAD_REQUEST)
    if Post.objects.filter(id=pk).exists():
        likes = Like.objects.filter(post=pk, user=request.data['user'])
        likes.delete()
        return Response({'message': 'Deleted !'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'post not found'}, status=status.HTTP_400_BAD_REQUEST)
