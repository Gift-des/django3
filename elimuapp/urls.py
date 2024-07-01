
from django.contrib import admin
from django.urls import path
from elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('info', views.information, name='info'),
    path('info2', views.information2,name='info2'),
    path('Form', views.Form, name='Form'),
    path('Login', views.Login, name='Login'),
    path('Registration', views.Registration, name='Registration'),

]
