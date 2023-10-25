from django.urls import path
from .views import RegisterView, all_post_view, CustomLoginView, MyPostListView, Detail_Blogpost_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('post/<slug:slug>/', Detail_Blogpost_view.as_view(), name='post_detail'),
    path('', all_post_view.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('myposts/', MyPostListView.as_view(template_name='users/myposts.html'), name='mypostspage')
]
