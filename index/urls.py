from django.urls import path

from index.views import index, problem, health

urlpatterns = [
    path('', index, name='index'),
    path('problem/', problem, name='problem'),
    path('health/', health, name='health'),
]
