from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name="indexfile"),
    path('ABOUTUS', views.about, name="ABOUTUSfile"),
    path('sports',views.sports, name="sports"),
    path('entertainment',views.entertainment, name="entertainment"),
    path('technology',views.technology, name="technology"),
    path('business',views.business, name="business"),
]