from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio-index'),
    path('portfolio/', views.portfolio, name='portfolio-portfolio'),
    path('service/', views.service, name='portfolio-service'),
    path('contact/', views.contact, name='portfolio-contact'),
    path('login/', views.login, name='portfolio-login'),
    path('thanks/', views.thanks, name='portfolio-thanks'),
]