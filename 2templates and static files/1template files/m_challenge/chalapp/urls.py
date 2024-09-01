from django.urls import path
from . import views

urlpatterns= [

    path("", views.index, name="home"),
    
    path("<month2>", views.chal, name="chal_mont")

]