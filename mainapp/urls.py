from django.conf import settings
import mainapp.views as mainapp
from django.urls import path
from django.conf.urls.static import static

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)