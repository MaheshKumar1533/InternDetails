from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('departments/', views.departments, name='departments'),
    path('noAccess/',views.noAccess,name='noAccess'),
    path('', views.login, name='login'),
    path('cse', views.department, name='department'),
]
# air37265