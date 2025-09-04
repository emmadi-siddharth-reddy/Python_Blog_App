from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('post/',views.all_posts, name='post')
]
