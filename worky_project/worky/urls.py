from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('blog', views.blog, name='blog'),
    path('log_in_admin', views.log_in_admin, name='log_in_admin'),
    path('log_out_admin', views.log_out_admin, name='log_out_admin'),
    path('admin_profile/<str:admin_username>', views.admin_profile, name='admin_profile'),
    path('create_post', views.create_post, name='create_post'),
    path('post/<int:post_id>', views.post, name='post')
]
