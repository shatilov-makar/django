from django.urls import path
from . import views

urlpatterns = [
    path('news', views.news_home, name='news'),
    path('create', views.create, name='create'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]
