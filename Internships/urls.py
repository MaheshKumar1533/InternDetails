from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('departments/', views.departments, name='departments'),
    path('noAccess/',views.noAccess,name='noAccess'),
<<<<<<< HEAD
    path('Details/',views.Details,name="Details"),
    #path('AccessFinder/',views.AccessFinder,name='AccessFinder')
    
=======
    path('', views.login, name='login'),
    path('cse', views.department, name='department'),
>>>>>>> c0c822cceca5d9bbe30a89aab0d60df9c7b80bf5
]
# air37265