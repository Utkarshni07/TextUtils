
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index2,name='index2'),
    path('analyze2/',views.analyze2,name='analyze2')
]
