from django.urls import path
from .views import *

urlpatterns = [
    
    path('',index,name='index'),
    path('createBlog/',createBlog,name = 'createBlog'),
    path('signin_page/',signin_page,name='signin_page'),
    path('login_page/',login_page,name='login_page'),
    path('single_blog_view/<pk>/',single_blog_view,name='single_blog_view'),
    path('update_blog/<pk>/',update_blog,name='update_blog'),
    path('delete_blog/<pk>/',delete_blog,name='delete_blog'),
    path('logout_page/',logout_page,name='logout_page')


]
