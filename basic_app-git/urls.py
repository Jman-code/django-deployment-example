from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('test/', views.test, name='test'),
    path('index2/', views.index2, name='index2'),
    path('log_in/', views.log_in, name='log_in'),
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)