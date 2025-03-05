from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path('', views.home, name='home'),
    path('add/', views.add, name='add_affiliate'),
    path('admin/', views.admin, name='admin'),
    path('login', views.login_view, name='login'),
    path('logout', views.out, name='logout'),
    path('base', views.base, name='base'),
    path('search/', views.search_products, name='search'),
    path('update/<int:id>', views.update_affiliate, name='update'),
    path('delete/<int:id>/', views.delete_affiliate, name='delete'),

     
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)