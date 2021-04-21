from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pdfparser.urls')),
    path('home/', include('pdfparser.urls')),
    path('upload/', include('pdfparser.urls')),
]
