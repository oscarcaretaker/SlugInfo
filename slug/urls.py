from django.urls import path, include


from . import views

urlpatterns = [
   path('', views.get_protoform_image, name='get_protoform_image'),
   path('<str:slug>',views.details, name='details'),
   path('search/', views.search_view, name='search_results'),

]