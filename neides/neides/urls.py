"""
URL configuration for neides project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from views import item_list, item_create, item_update, item_delete



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
    path('item/new/', item_create, name='item_create'),
    path('item/<int:pk>/edit/', item_update, name='item_update'),
    path('item/<int:pk>/delete/', item_delete, name='item_delete'),
    path('admin/', admin.site.urls),
    path('', include('neides_app')),  
]