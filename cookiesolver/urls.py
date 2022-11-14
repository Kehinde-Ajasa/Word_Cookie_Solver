from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("Solution",views.solution,name="solution"),
    path("About",views.about,name="about"),


    # apis
    path('getUserInput',views.getUserInput,name="getUserInput"),
    path('retrieve',views.retrieve,name="retrieve")
]