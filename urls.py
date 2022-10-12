"""fswd URL Configuration

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
from . import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.home, name='home'),
    path('signup/',index.signup,name='signup'),
    path('login/',index.login,name='login'),
    path('about/', index.about, name='about'),
    path('faq/', index.faq, name='faq'),
    path('our_services/', index.our_services, name='our_services'),
    path('privacy_policy/', index.privacy_policy, name='privacy_policy'),
    path('facebook/', index.facebook, name='facebook'),
    path('twitter/', index.twitter, name='twitter'),
    path('instagram/', index.instagram, name='instagram'),
    path('linkedin/', index.linkedin, name='linkedin'),
    path('email/', index.email, name='email'),
    path('courses/', index.courses, name='courses'),
    path('ComCourse/', index.ComCourse, name='ComCourse'),
    path('ScCourse/', index.ScCourse, name='ScCourse'),
    path('pay/', index.payment, name='pay'),

]
