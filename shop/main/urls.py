from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('brands/', views.brands, name='brands'),
    path('catalog/', views.product_list, name='product_list'),
    path('brands/', views.brands, name='brands'),
    path('contacts/', views.contacts, name='contacts'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
