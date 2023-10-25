from django.urls import path
from .views import RegisterView, BlogListView,Detail_Blogpost_view,CustomLoginView,MyPostListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('<int:pk>/',Detail_Blogpost_view.as_view(),name = 'detail_blogpost'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('myposts/', MyPostListView.as_view(template_name='users/myposts.html'), name='mypostspage')
]
