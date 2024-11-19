from django.contrib import admin
from django.urls import path, include
from classnest_Base.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classnest_Base.urls')),
    path('profile/', profile_view, name='profile'),
]
