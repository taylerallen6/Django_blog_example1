from django.urls import path, include

from . import views


app_name = 'posts'
urlpatterns = [
    path('<pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
