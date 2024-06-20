"""
URL configuration for mytodo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from todo.views import todo_list, add_item, toggle_complete, delete_item

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_item, name='add_item'),
    path('toggle_complete/<int:item_id>/', toggle_complete, name='toggle_complete'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]
