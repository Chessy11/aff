from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from userforms.views import user_forms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('homepage.urls')),
    path('about/', views.about_us, name='about_us'),
    path('whyus/', views.why_us, name='why_us'),
    path('team/', views.team, name='team'),
    path('user_forms', user_forms, name='user_forms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
