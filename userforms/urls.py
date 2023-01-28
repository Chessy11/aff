from django.urls import path
from . import views 

urlpatterns = [
    path('', views.user_forms, name='user_form'),
]

app_name = 'userforms'