"""hyperflex_recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from hyperflex import views as fun

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^swagger/$', schema_view),
    #
    url(r'^hyperflex/get_tianmao_voice_answer$', fun.get_tianmao_voice_answer, name='get_tianmao_voice_answer'),
    #
    url(r'^hyperflex/recipe_recommended$', fun.recipe_recommended, name='recipe_recommended'),
    #
    url(r'^hyperflex/user_analysis$', fun.user_analysis, name='user_analysis')
]
