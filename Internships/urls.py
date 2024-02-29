from django.urls import path
from . import views
from django.conf.urls.static import static
from InternDetails import settings

urlpatterns = [
    path('', views.primaryDashboard, name='primaryDashboard'),
    path('custom_login/', views.custom_login, name='custom_login'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('register_form', views.register_form, name='register_form'),
    path('bulkdata/', views.bulk_data_input, name='bulk_data_input'),
    path('ExclusiveDashboard/', views.ExclusiveDashboard, name='ExclusiveDashboard'),
    path('noAccess/',views.noAccess,name='noAccess'),
    path('Details/',views.Details,name="Details"),
    path('create_student',views.create_student,name="create_student"),
    path('addInternship',views.addInternship,name='addInternship'),
    path('forgotPassword',views.forgotPassword,name='forgotPassword'),
    #path('AccessFinder/',views.AccessFinder,name='AccessFinder')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# air37265