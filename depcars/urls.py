"""depcars URL Configuration

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
from django.conf.urls import url,include
from user.views import home
from user import views
urlpatterns = [
    url('admin/', admin.site.urls), 
    url(r'^home', home,name='home'),
    url(r'^delete/(?P<pk>\d+)',views.delete, name='delete'),
    url(r'^edit/(?P<pk>\d+)', views.edit, name='edit'),    
    url(r'^user/add/$',views.add, name='add'),
    #url(r'', include('user.urls')),
]


