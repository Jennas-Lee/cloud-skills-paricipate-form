from django.urls import path

from account.views import account, mypage, aws, signin, signout

urlpatterns = [
    path('', account, name='account'),
    path('mypage/', mypage, name='mypage'),
    path('aws/', aws, name='aws'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
]
