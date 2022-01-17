from django.urls import path

from index.views import index, problem

urlpatterns = [
    path('', index, name='index'),
    path('problem/', problem, name='problem')
]
