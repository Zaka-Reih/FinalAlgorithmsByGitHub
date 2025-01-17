from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('popular_posts', views.PopularPosts, name='popular_posts'),
    path('fresh_posts', views.FreshPosts, name='fresh_posts'),
    path('my_subscription', views.MySubscription, name='my_subscription'),
]
