"""hypernews URL Configuration

The `urlpatterns` list routes URLs to templates. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function templates
    1. Add an import:  from my_app import templates
    2. Add a URL to urlpatterns:  path('', templates.home, name='home')
Class-based templates
    1. Add an import:  from other_app.templates import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import MainPageView, NewsPage, NewsHomePage, NewsCreatePage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view()),
    path('news/<int:news_id>/', NewsPage.as_view()),
    path('news/', NewsHomePage.as_view()),
    path('news/?<str:q>/', NewsHomePage.as_view()),
    path('news/create/', NewsCreatePage.as_view()),
]

urlpatterns += static(settings.STATIC_URL)
