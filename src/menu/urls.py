from django.urls import path

from .views import index

app_name = 'menu'


urlpatterns = [
    path('<slug:slug>/', index, name='index'),
]
