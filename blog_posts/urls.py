from rest_framework.routers import SimpleRouter
from blog_posts import views
from django.urls import path


urlpatterns = [
    path('post/read/', views.get_all_posts),
    path('post/create/', views.create_post),
    path('post/delete/<int:id>/', views.delete_post),
    path('post/update/<int:id>/', views.update_post),
    path('post/get/<int:id>/', views.get_blog_details),
    path('post/get/<int:id>/comment/create/', views.create_comment),
    path('post/get/<int:id>/comment/delete/<int:cid>/', views.delete_comment),
    path('post/get/<int:id>/comment/update/<int:cid>/', views.update_comment),

]