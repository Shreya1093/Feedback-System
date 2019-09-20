"""feedback_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import register
from users.views import validate
from users.views import temp
from users.views import home
from users.views import co
from django.contrib.auth import views
from users.views  import feedback_create_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='users/Login.html'), name='login'),
    path('login/validate/', validate,name='validate'),
    path('logout/', views.LoginView.as_view(template_name='users/temp.html'), name='logout'),
    path('temp/', temp, name='temp'),
    path('home/',home,name='home'),
    path('co/<str:sem>', co, name='co'),
    path('feedback/',feedback_create_view),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)