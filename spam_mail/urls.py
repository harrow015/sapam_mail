"""spam_mail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from site_admin import views as admin_views
from user import views as user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',admin_views.index,name="index"),
    path('login/',admin_views.login,name="login"),
    path('loginaction/',admin_views.loginaction,name="loginaction"),
    path('addhobby/',admin_views.addhobby,name="addhobby"),
    path('addhobbyaction/',admin_views.addhobbyaction,name="addhobbyaction"),
    path('addfactor/',admin_views.addfactor,name="addfactor"),
    path('addfactoraction/',admin_views.addfactoraction,name="addfactoraction"),
    path('addseason/',admin_views.addseason,name="addseason"),
    path('addseasonaction/',admin_views.addseasonaction,name="addseasonaction"),
    path('addseasonfactor/',admin_views.addseasonfactor,name="addseasonfactor"),
    path('addseasonfactoraction/',admin_views.addseasonfactoraction,name="addseasonfactoraction"),
    path('register/',user_view.register,name="register"),
    path('getstate/',user_view.getstate,name="getstate"),
    path('registeraction/',user_view.registeraction,name="registeraction"),
    path('sendmessage/',user_view.sendmessage,name="sendmessage"),
    path('checkuser/',user_view.checkuser,name="checkuser"),
    path('sendmessageaction/',user_view.sendmessageaction,name="sendmessageaction"),
    path('viewrecivedmessage/',user_view.viewrecivedmessage,name="viewrecivedmessage"),
    path('movetotrash/',user_view.movetotrash,name="movetotrash"),
    path('forwardmessage<int:id>/',user_view.forwardmessage,name="forwardmessage"),
    path('forwardmessageaction/',user_view.forwardmessageaction,name="forwardmessageaction"),
    path ('viewsendmessage/',user_view.viewsendmessage,name="viewsendmessage"),
    path('viewsendmessage/',user_view.viewsendmessage,name="viewsendmessage"),
]
