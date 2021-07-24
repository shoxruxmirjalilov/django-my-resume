from django.urls import path

from . import views

urlpatterns = [
   path('', views.PostIndexView.as_view(), name='index'),
   path('<int:pk>/post/', views.PostDetailView.as_view(), name='post'),
   path('search/', views.Search.as_view(), name='search')

]    
   
