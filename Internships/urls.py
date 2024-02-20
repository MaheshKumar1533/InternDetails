from django.urls import path
from . import views
from django.conf.urls.static import static
from InternDetails import settings

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.bulk_data_input, name='bulk_data_input'),
    path('departments/', views.departments, name='departments'),
    path('noAccess/',views.noAccess,name='noAccess'),
    path('Details/',views.Details,name="Details"),
    path('create_student',views.create_student,name="create_student"),
    #path('AccessFinder/',views.AccessFinder,name='AccessFinder')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# air37265