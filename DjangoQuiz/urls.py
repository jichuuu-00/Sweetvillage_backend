"""DjangoQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from account.views import *
from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('question/', question,name='question'),
    path('makevisitor/', makevisitor, name='makevisitor'),
    path('visitor/', visitor, name='visitor'),
    #path('login/', login,name="login"),
    #path('logout', logout, name='logout'),
    #path('signup/',signup, name="signup"),
    path('account/',include('account.urls')),
    # path('login/', loginPage,name='login'),
    # path('logout/', logoutPage,name='logout'),
    # path('register/', registerPage,name='register'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
