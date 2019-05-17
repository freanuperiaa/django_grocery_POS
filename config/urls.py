from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('apps.grocery.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('transaction/', include('apps.transaction.urls')),
]
