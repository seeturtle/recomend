from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),
    path('post', views.post, name='post'),
    path('comment', views.comment, name='comment'),
]
