from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView

urlpatterns = [
    path('', BlogPostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post-delete'),
]