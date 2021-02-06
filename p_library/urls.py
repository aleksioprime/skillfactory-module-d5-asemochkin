from django.urls import path  
from .views import index, return_book, BookFriendEdit, BookAdd, FriendAdd

app_name = 'p_library'
urlpatterns = [
    path('index/', index, name='index'),
    path('index/return_book/', return_book, name='return_book'),
    path('index/book_add/', BookAdd.as_view(), name='book_add'),
    path('index/<int:pk>/book_friend_edit/', BookFriendEdit.as_view(), name='book_friend_edit'),
    path('index/friend_add/', FriendAdd.as_view(), name='friend_add'),
]
