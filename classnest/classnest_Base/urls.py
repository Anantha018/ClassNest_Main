# classnest_Base/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import profile, reset_password, logout_view
from .views import home

from django.urls import path, include  # Add 'include'

    
urlpatterns = [
    path('', home, name='home'), # Root URL for homepage or dashboard
    
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create-course/', views.create_course_view, name='create-course'),
    path('courses/', views.courses_view, name='courses'),
    path('course/<int:course_id>/', views.course_detail_view, name='course-detail'),
    path('course/delete/<int:course_id>/', views.delete_course_view, name='delete-course'),
    path('login/', auth_views.LoginView.as_view(template_name='classnest_Base/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='classnest_Base/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='classnest_Base/password_change_done.html'), name='password_change_done'),
    
    path('profile/', profile, name='profile'),
    path('reset-password/', reset_password, name='reset_password'),
    path('logout/', logout_view, name='logout'),
    
    # Include Django's built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)