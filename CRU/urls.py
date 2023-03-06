from django.urls import path
from . import views

urlpatterns = {
    path('intro', views.intro),
    path('smth', views.smth)
}
