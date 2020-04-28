from django.contrib import admin
from django.urls import path
from src.blog import views

urlpatterns = [
    path('idontexist/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
