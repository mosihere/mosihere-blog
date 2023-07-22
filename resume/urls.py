from django.urls import path
from . import views


app_name = 'resume'

urlpatterns = [
    path('', views.main_page, name='home')
]
