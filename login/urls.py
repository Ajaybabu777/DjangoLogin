from django.urls import path
from login import views
urlpatterns = [
    path('registeruser/',views.registeruser,name='registeruser'),
    path('login/',views.login,name = 'login'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
]
