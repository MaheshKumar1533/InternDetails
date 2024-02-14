from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('departments/', views.departments, name='departments'),
    path('noAccess/',views.noAccess,name='noAccess'),
    path('Details/',views.Details,name="Details"),
    path('create_student',views.create_student,name="create_student"),
    #path('AccessFinder/',views.AccessFinder,name='AccessFinder')
    
]
# air37265