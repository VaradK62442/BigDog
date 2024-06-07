from django.urls import path
from notes import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
]