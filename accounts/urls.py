from django.urls import path

from .views import SearchProfileView
from .views import MessageView, get_all_message, get_new_message
from .views import ProfileMixinView, ProfileMixinViewGetById, get_profile_by_userId
from .views import FriendMixinView, FriendMixinViewByUserId, check_is_friend
from .views import PostMixinView, ListPostUserMixinView, ListPostMixinView
from .views import CommentMixinView, CommentMixinViewGetByUSerId
from .views import ConversationMixinView, ConversationMixinViewGetByUserId
from .views import CreateLikeMixinView, ListPostMixinView, count_numbers_like, check_user_is_liked, remove_like_post
from .views import SearchProfileView


urlpatterns = [
    path('user/search', SearchProfileView.as_view()),

    path('profile/<int:pk>', ProfileMixinView.as_view()),
    path('profile/get/<int:pk>', ProfileMixinViewGetById.as_view()),
    path('profile/user/<int:pk>', get_profile_by_userId),

    path('friend/<int:pk>', FriendMixinView.as_view()),
    path('friend/all/<int:pk>', FriendMixinViewByUserId.as_view()),
    path('friend/is_friend/<int:pk>', check_is_friend),

    path('post/<int:pk>', PostMixinView.as_view()),
    path('post/all/<int:pk>', ListPostUserMixinView.as_view()),
    path('post', ListPostMixinView.as_view()),

    path('comment/<int:pk>', CommentMixinView.as_view()),
    path('comment/post/<int:pk>', CommentMixinViewGetByUSerId.as_view()),

    path('conversation/<int:pk>', ConversationMixinView.as_view()),
    path('conversation/user/<int:pk>', ConversationMixinViewGetByUserId.as_view()),

    path('message/<int:pk>', MessageView.as_view()),
    path('message/all/<int:pk>', get_all_message),
    path('message/get/new/<int:pk>', get_new_message),

    path('like/create', CreateLikeMixinView.as_view()),
    path('like/remove/<int:pk>', remove_like_post),
    path('like/count/<int:pk>', count_numbers_like),
    path('like/check/<int:pk>', check_user_is_liked),
]