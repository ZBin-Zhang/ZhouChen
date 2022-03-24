app_name = 'BearingErrors'

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test, name='test'),
    path('welcome', views.welcome, name='welcome'),
    path('bearing_info', views.bearing_info, name='bearing_info'),
    path('tree', views.show_tree, name='tree'),
    path('bearing_process', views.bearing_process, name='BP'),
    path('BearingErrors/dashboard/', views.welcome, name='test'),
]
