from django.urls import path


from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfilesView.as_view())
] 
#http://127.0.0.1:8000/profiles/