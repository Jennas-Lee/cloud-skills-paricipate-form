from django.contrib import admin
from django.urls import path, include

from account.urls import urlpatterns as account_urls
from index.urls import urlpatterns as index_urls

urlpatterns = [
    path('', include(index_urls)),
    path('account/', include(account_urls)),

    path('admin/', admin.site.urls),
]
