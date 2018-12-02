from django.urls import path

from .views import basket_add

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:pk>', basket_add, name='add'),
]
