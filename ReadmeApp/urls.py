from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('htmlpage/', views.HTMLGenerator.as_view(), name='htmlpage')
]
