"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views
app_name = 'l_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows the topics
    path('topics/', views.topics, name='topics'),
    # Individual page for every topic
    path('topics/<int:topic_id>', views.topic, name = 'topic'),
    # Page that shows other topics that nobody cares
    path('topicsno/', views.topicsno, name = 'topicsno'),
    ]