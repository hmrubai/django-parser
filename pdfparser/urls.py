from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="pdf"),
    path('image/', views.HomeView.as_view(), name="pdf"),
    path('file/', views.UploadFileView.as_view(), name="pdf"),
]