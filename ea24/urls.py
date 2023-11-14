"""
URL configuration for ea24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView ,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name="home"),
    path('news',news_view,name="news"),
    path('signup/',sign,name="signup"),
    path('login',CustomLoginView.as_view(template_name='main/auth_login.html'),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('community',comview,name="compage"),
    path('dislike/<int:pk>',dislikeview,name='dislike_page'),
    path('like/<int:pk>',likeview,name='like_page'),
    path('post_p/<post_id>',postpagedef,name="post_page"),
    path('updateprofile',my_accountdef,name="profile"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)