from django.urls import path
from . import views

app_name = 'newsapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news-detail/<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),

    path('seizi/', views.SeiziView.as_view(), name='seizi'),
    path('sports/', views.SportsView.as_view(), name='sports'),
    path('tenki/', views.TenkiView.as_view(), name='tenki'),

    # 記事投稿・削除機能の追加
    path('post/create/', views.post_create, name='post_create'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    

]
