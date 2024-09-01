from django.urls import path
from . import views

urlpatterns= [

    path("", views.index), #blank means  /challen/ from monthly_chall project
    
    path("<month2>", views.chal, name="chal_mont")

]