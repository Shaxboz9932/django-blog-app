from django.urls import path
from .views import (BlogListView,
                    BlogDetailView,
                    BlogEditView,
                    BlogCreateView,
                    BlogDeleteView,
                    )

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', BlogEditView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'),

]