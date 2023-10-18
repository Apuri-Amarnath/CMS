from django.urls import path
from .views import RegisterView, BlogListView,Detail_Blogpost_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('<int:pk>/',Detail_Blogpost_view.as_view(),name = 'detail_blogpost'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
