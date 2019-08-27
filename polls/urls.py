from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/recommends/<int:recommend_id>/best', views.set_best_recommend, name='set_best_recommend'),
    path('post', views.post, name='post'),
    path('comment', views.comment, name='comment'),
]
