from django.urls import path

from labSoft3 import views

urlpatterns = [
    path("", views.metzli, name='METZLI'),
    path("menu", views.menu, name= 'menu'),
    path("sugerencias",views.sugerencias, name='sugerencias'),

]
