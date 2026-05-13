from django.urls import path, include

from blog.apps import BlogConfig
# from blog.views import index

from blog.views import BlogBaseView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name


urlpatterns = [
    # path('', index),
    path('base/', BlogBaseView.as_view(), name='base'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]