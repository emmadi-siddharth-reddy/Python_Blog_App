from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<int:id>/edit', views.post_edit, name = 'post_edit'),
    path('post/<int:id>/delete', views.post_delete, name='post_delete'),
    path('api/posts/', views.PostListAPI.as_view(), name='api_posts'),
    path('api/posts/<int:id>', views.PostDetailAPI.as_view(), name='api_post_detail'),
]
