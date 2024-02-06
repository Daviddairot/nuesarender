from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('admin/', admin.site.urls, namespace = 'admin'),
    path('', views.index, name="index"),
    path('next_page/', views.next_page, name='next_page'),
    path('next/', views.login_view, name='next'),  # 'next' is the login page
    path('vote/', views.vote, name='vote'),
    path('end/', views.end, name='end'),
    path('vote_submit/', views.vote_submit, name='vote_submit'),
    path('close/', views.close, name='close'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
