from django.urls import path, include
from .views import PostList, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, PostSearch



urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали 
    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание 
    path('edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
]